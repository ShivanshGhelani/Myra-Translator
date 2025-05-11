from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
import mtranslate as mt
import logging
from langdetect import detect, detect_langs

router = APIRouter()

class TranslationRequest(BaseModel):
    text: str
    dest_lang: str = "en"
    source_lang: Optional[str] = Field(
        default=None, 
        description="Source language code. If not provided, will be auto-detected"
    )
    preserve_formatting: bool = Field(
        default=True,
        description="Preserve original text formatting (newlines, spaces)"
    )
    auto_detect: bool = Field(
        default=True,
        description="Whether to auto-detect the source language"
    )
    char_limit: Optional[int] = Field(
        default=None,
        description="Maximum number of characters to translate",
        gt=0
    )

def normalize_language_code(lang_code: str) -> str:
    # Map special cases for language codes
    lang_map = {
        "zh-CN": "zh",  # Simplified Chinese
        "zh-TW": "zh-TW",  # Traditional Chinese
    }
    return lang_map.get(lang_code, lang_code)

def detect_language(text: str) -> tuple[str, float]:
    """Detect the language of the text and return language code with confidence score."""
    try:
        # Get all possible languages with probabilities
        languages = detect_langs(text)
        # Return the most probable language and its confidence
        if languages:
            return languages[0].lang, languages[0].prob
        return "en", 0.0
    except:
        return "en", 0.0

@router.post("/translate")
async def translate(request: TranslationRequest):
    try:
        # Validate text length
        if request.char_limit and len(request.text) > request.char_limit:
            raise HTTPException(
                status_code=400, 
                detail=f"Text exceeds maximum length of {request.char_limit} characters"
            )

        # Handle source language
        source_lang = request.source_lang
        detection_confidence = None
        
        if request.auto_detect and not source_lang:
            source_lang, detection_confidence = detect_language(request.text)

        # Normalize the language codes
        normalized_dest_lang = normalize_language_code(request.dest_lang)
        
        # Perform translation
        text_to_translate = request.text
        if not request.preserve_formatting:
            # Remove extra whitespace while preserving single spaces between words
            text_to_translate = " ".join(request.text.split())

        # mtranslate only accepts target language, it auto-detects source language
        translated_text = mt.translate(text_to_translate, normalized_dest_lang)

        # Prepare response
        response = {
            "translated_text": translated_text,
            "source_text": request.text,
            "target_language": request.dest_lang,
            "detected_source_language": source_lang,
            "detection_confidence": detection_confidence if detection_confidence is not None else None,
            "preserved_formatting": request.preserve_formatting
        }

        return JSONResponse(content=response)

    except Exception as e:
        logging.error(f"Translation error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")