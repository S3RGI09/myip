echo "Bienvenido al asistente de instalacion de myip, vamos a empezar por instalar las librerias de python."
pip install socket
echo "Si te da error significa que ya las tienes instaladas o que tu version de python no es la adecuada, recuerda, Python3"
echo "ahora vamos a darle permisos de ejecucion al script, esto SOLO FUNCIONA EN SISTEMAS UNIX-LIKE"
chmod +x myip.py
echo "Ahora solo pon en tu consola "./myip.py" ya tienes el script listo"
echo "Gracias por instalar myip, ahora vamos a borrar este instalador"
rm instalacion.sh
