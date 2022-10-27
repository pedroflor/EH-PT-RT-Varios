for i in $(netstat -antp | grep CLOSE | awk -F " " '{ print $7}' | cut -f1 -d"/")
do
   kill $i
done
