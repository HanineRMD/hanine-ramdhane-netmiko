# Mon Projet Netmiko
# Initialiser un dépôt Git local
 mkdir hanine-ramdhane-netmiko
 
 cd hanine-ramdhane-netmiko
 
 git init

# Ajouter et commiter des fichiers
echo "# Mon Projet Netmiko" > README.md

git add README.md

git commit -m "ajoute le fichier readme.md" 

echo 'print("Hello, Git!")' > main.py

git add main.py

git commit -m "Ajout du script Python principal"

git log --oneline

# Créer et fusionner des branches

git checkout -b feature/netmiko

Modification main.py

git add main.py

git commit -m "ajout de contenu main.py"

git checkout main

git checkout -b feature/netmiko

git merge feature/netmiko

# Travailler avec un dépôt distant sur GitHub

git remote add origin https://github.com/HanineRMD/hanine-ramdhane-netmiko.git

git branch -M main

git push -u origin main

git fetch origin

git checkout -b feature/salut origin/feature/salut

git add main.py

git commit -m "2eme ajout de contenu main.py"

git push origin feature/salut
