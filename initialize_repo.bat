@echo off
echo Initializing GitHub repository for Universal Translator...

echo Step 1: Initializing Git repository...
git init

echo Step 2: Adding files to repository...
git add .

echo Step 3: Creating initial commit...
git commit -m "Initial commit of Universal Translator project"

echo Step 4: Setting up the main branch...
git branch -M main

echo.
echo Repository initialized successfully!
echo.
echo Next steps:
echo 1. Create a new repository on GitHub
echo 2. Connect to your remote repository using:
echo    git remote add origin https://github.com/ShivanshGhelani/Myra-Translator.git
echo 3. Push your code using:
echo    git push -u origin main
echo.
echo Then follow the Vercel deployment instructions in the README.md file.
