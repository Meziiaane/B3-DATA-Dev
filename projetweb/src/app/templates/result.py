import cgi
import cgitb
import mysql.connector
from flask import Flask, redirect

link = mysql.connector.connect(
    host='mysql',
    database = 'rna',
    user='root',
    password =""
)
cur = link.cursor()


#Récupération des donnés du formulaire
form = cgi.FieldStorage()
rnaId = form.getvalue("rnaId")
rnaIdEx = form.getvalue("rnaIdEx")
gestion = form.getvalue("gestion")

# Ajout d'une ligne à une table
add_line = "INSERT INTO data (rna_id, rna_id_ex, gestion) VALUES (%s, %s, %s)"
cur.execute(add_line, (rnaId,rnaIdEx, gestion ))
link.commit()

# Fermeture de la connexion
cur.close()
link.close()

redirect('/assos')

# # Redirection vers la page de confirmation
# print("Content-type:text/html\r\n\r\n")
# print("<html>")
# print("<head>")
# print("<title>Ajout de produit réussi</title>")
# print("</head>")
# print("<body>")
# print("<h2>Le produit " + rnaId + " a été ajouté avec succès à la table ma_table.</h2>")
# print("</body>")
# print("</html>")
