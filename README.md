# New project: MSE800

…or create a new repository on the command line

echo "# MSE800" >> README.md

git init

git add README.md

git commit -m "first commit"

git branch -M main

git remote add origin https://github.com/lordong/MSE800.git

git push -u origin main ('git push origin' will use the default branch - main)



…or push an existing repository from the command line

git remote add origin https://github.com/lordong/MSE800.git

git branch -M main

git push -u origin main

# Related command

1. Download and install Anaconda from [https://www.anaconda.com/](https://www.anaconda.com/)

2. Run **Anaconda Powershell Prompt** from the Start menu

3. Use **conda env list** to list the environments of Anaconda

4. Use **conda create --name Envname python=version** to create an environment for a specific project (run **python** to check the version first)

5. Use **conda activate Envname** to activate the environment

6. Use **pip install packagename** to install a new package, e.g. **pip install numpy**
