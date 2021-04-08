A.
    i.   YAML file is pod1-hw5.yml, command is kubectl apply -f pod1-hw5.yml
    ii.  kubectl get pod greeting-personalized
    iii. It's Hello, !. I expected that because we didn't assign a value to the NAME variable.
    iv.	 kubectl delete pods greeting-personalized
B.
    i.   YAML File is pod2-hw5.yml, command is kubectl apply -f pod2-hw5.yml
    ii.	 kubectl logs greeting-personalized-name. Output is Hello, Jeremy!
    iii. kubectl delete pods greeting-personalized-name
C. 
    i.   YAML file is deployment-hw5.yml, command is kubectl apply -f deployment-hw5.yml
    ii.  kubectl get pods -l app=hw5-app
    iii. kubectl logs -l app=hw5-app. Output is 
             Hello, Jeremy from IP 10.244.6.207
             Hello, Jeremy from IP 10.244.5.150
             Hello, Jeremy from IP 10.244.7.191
    iv.  Yes, they match.
             kubectl logs deployment-hw5-565b8d54c4-bj2sx
             Hello, Jeremy from IP 10.244.6.207
             kubectl logs deployment-hw5-565b8d54c4-kdxk2
             Hello, Jeremy from IP 10.244.5.150
             kubectl logs deployment-hw5-565b8d54c4-zzkjb
             Hello, Jeremy from IP 10.244.7.191

