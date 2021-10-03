# runs sample files
for i in {0..1}
do
    echo $i
    python3 solutions/sol.py < samples/input/input$i.txt > samples/output/output$i.txt
done
