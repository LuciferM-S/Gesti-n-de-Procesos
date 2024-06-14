if [ -z "$1" ]; then
    echo "Uso: $0 <intervalo_en_segundos>"
    exit 1
fi

intervalo=$1

archivo="recursos.csv"

tiempo=0

echo "Tiempo-CPU-MEM" > "$archivo"

obtener_datos() {
   datosCPU=$(top -b -n 1 | awk '/^%Cpu/ {print $4}')
   datosMEM=$(top -b -n 1 | awk '/^MiB Mem/ {print $8}')
   echo "$tiempo-$datosCPU-$datosMEM" >> "$archivo"
   echo >> "$archivo"
   tiempo=$((tiempo + intervalo))
}

while true; do
    obtener_datos
    sleep "$intervalo"
done
