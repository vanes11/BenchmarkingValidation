from genericpath import isdir
import os
import sys
import glob
import csv
import re
import copy
import json
from UniformQuickFill import UniformQuickFill
from InteractQuickFill import InteractQuickFill
from deepdiff import DeepDiff

# recuperation du parametre qui indique le cas d'utilisation des donnees (FlashFill ou QuickFill ou FlashFill&QuickFill)


#print(os.getcwd(),"......")

def Pretraitement():
    """ stockage des chemins vers les fichiers de chaque benchmarks, dependament 
    du fait que nous voulons les resultats de FlahFill,QuickFill ou des deux."""
    arg = sys.argv
    currentDirectory = os.getcwd()
    repositories = [i for i in os.listdir(currentDirectory) if os.path.isdir(currentDirectory+'/'+i)]
    repositories.sort()

    if len(arg)>1:
        
        if arg[1] == 'F':
            
            SousDossier = [i for i in os.listdir(currentDirectory+'/'+repositories[0]) if os.path.isdir(currentDirectory+'/'+repositories[0]+'/'+i)]          
            sousChemin = {}
            
            for repository in SousDossier:
                Chemins = {}
                FileList = glob.glob(currentDirectory+'/'+repositories[0]+'/'+repository+'/*.csv')
               
                
                for elt in FileList:

                        chemin = elt.split('/')
                        chemin = chemin[-1]
                        chemin = chemin.split('.')
                        chemin = chemin[0]
                       
                        if len(chemin)== 1:
                            Chemins[chemin]= elt           
                
                sousChemin[repository] = Chemins
                
            return sousChemin

            
        elif arg[1] == 'Q':
            
            SousDossier = [i for i in os.listdir(currentDirectory+'/'+repositories[1]) if os.path.isdir(currentDirectory+'/'+repositories[1]+'/'+i)]          
            
            sousChemin = {}
            for repository in SousDossier:
                Chemins = {}
                FileList = glob.glob(currentDirectory+'/'+repositories[1]+'/'+repository+'/*.csv')
                
                for elt in FileList:
                    
                        chemin = elt.split('/')
                        chemin = chemin[-1]
                        chemin = chemin.split('.')
                        chemin = chemin[0]
                       
                        if len(chemin)== 1:
                            Chemins[chemin]= elt
                                           
                sousChemin[repository] = Chemins

            return sousChemin

    else:
        print("-----------------------------------------------\n Veillez entrer un argument : \n F pour travailler sur FlashFill \n Q pour travailler sur QuickFill \n D pour travailler sur les 2.")



def viderFichier():
    arg = sys.argv
    currentDirectory = os.getcwd()
    Chemin1 = currentDirectory+'/FlashFillResults/'
    Chemin2 = currentDirectory+'/QuickFillResults/'
    
    if  arg[1] == 'F':
        with open(Chemin1 + "ErorElements1.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "ErorElements2.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "ErorElements3.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "ErorElements4.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "FakePrograms1.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "FakePrograms2.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "FakePrograms3.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "FakePrograms4.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "GoodPrograms1.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "GoodPrograms2.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "GoodPrograms3.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "GoodPrograms4.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "Programs1.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "Programs2.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "Programs3.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "Programs4.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "stat1.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "stat2.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "stat3.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin1 + "stat4.txt", "w") as a_file:
            a_file.truncate()
        
        
    elif arg[1] == 'Q':

        with open(Chemin2 + "ErorElements1.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "ErorElements2.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "ErorElements3.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "ErorElements4.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "FakePrograms1.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "FakePrograms2.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "FakePrograms3.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "FakePrograms4.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "GoodPrograms1.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "GoodPrograms2.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "GoodPrograms3.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "GoodPrograms4.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "Programs1.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "Programs2.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "Programs3.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "Programs4.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "stat1.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "stat2.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "stat3.txt", "w") as a_file:
            a_file.truncate()
        with open(Chemin2 + "stat4.txt", "w") as a_file:
            a_file.truncate()



    
    

def Execution(Paths):
    """ Execution sur l'ensemble des benchmarks et retour des statiqques.
    l'argument Paths etant le resultat de l'excution de la fonction Pretraitement """
    arg = sys.argv
    currentDirectory = os.getcwd()
    viderFichier()
    chemin = ""
    chemin2 = ""
    ListeDesSorties = []
    ListeDesEntrees = []
    ListeOfProgrammes = []
    ListeOfGoodProgramme = []
    ListeOfBadProgramme = []
    ListeDesElementBonneReponse = []
    ListeOfFirstEroorElements = []
    CheminBonResultat = ""
    
    Test = []
    csv_reader = ""
    if len(arg) > 1:
        if arg[1] == 'F':
            #lecture des fichiers

            for key  in Paths:
                DicoBonneReposese = {}
                CheminBonResultat = currentDirectory+'/FlashFillResults/'+key + '/' +key.lower()+'.csv'
                       
                   
                for numero in Paths[key]:
                    
                    print("Debut Cas " + numero + " Benchmark " + key + "\n")
                    if numero == '1':
                        ListeDesSorties = []
                        ListeDesEntrees = []
                        ListeOfGoodProgramme = []
                        ListeOfBadProgramme = []
                        ListeDesElementBonneReponse = []
                        ListeOfFirstEroorElements = []
                        ResultatFinal = []
                        
                        with open(CheminBonResultat) as csv_file:
                            # gestion du fichier resultat contenant les entrees-sorties
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count = 0
                            for row in  csv_reader:
                                if line_count != 0:
                                    ListeDesElementBonneReponse.append("+++".join(row[:-1]) + '---' + row[-1])
                                    line_count += 1
                                else:
                                    line_count += 1
                        
                        with open(Paths[key][numero]) as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count = 0
                            for row in  csv_reader:
                                if line_count == 0:
                                    ListeDesSorties.append("+++".join(row[:-1]) + '---' + row[-1])
                                    line_count += 1
                                else:
                                    ListeDesEntrees.append("+++".join(row[:-1]))
                                    line_count += 1
                                    


                        chemin = currentDirectory +  '/data.txt'
                        chemin2 = currentDirectory + '/dataTest.txt'
                        chemin3 = currentDirectory + '/dataResult.txt'
                        filename = 'dataTest.txt'
                        
                        with open(chemin, 'w') as f:
                            f.write('\n'.join(ListeDesSorties))
                            
                        with open(chemin2, 'w') as f:
                            f.write('\n'.join(ListeDesEntrees))
                        
                        with open(chemin3, 'w') as f:
                            f.write('\n'.join(ListeDesElementBonneReponse))
                                               
                        
                        Test = UniformQuickFill()
                        Test.GetClassC()
                        DicoBonneReposese = Test.GetGoodExamples()
                        ListeOfProgrammes = list(Test.GenerateStringProgram3(Test.GetExamples()[0]))
                       
                        for prog in ListeOfProgrammes:
                            spetResultOne = Test.ExecuteOnElements(filename,prog)

                            if spetResultOne == DicoBonneReposese:
                                ListeOfGoodProgramme.append(prog)
                            else:
                                StepBadElement = (DeepDiff(DicoBonneReposese, spetResultOne))["values_changed"]
                                keyToPass,valueToPass = list(StepBadElement.items())[0]
                                keyToPass = keyToPass.replace('root[' ,'',1)
                                last_char_index = keyToPass.rfind("]")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                keyToPass = keyToPass.replace('{' ,'',1)
                                last_char_index = keyToPass.rfind("}")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                valueToPass = str(json.dumps(valueToPass))
                                valueToPass = valueToPass.replace('{' ,'',1)
                                last_char_index = valueToPass.rfind("}")
                                valueToPass = valueToPass[:last_char_index] +  valueToPass[last_char_index+1:]
                                ListeOfFirstEroorElements.append(keyToPass + " : " + valueToPass)
                                ListeOfBadProgramme.append(prog)

                        
                        if len(ListeOfProgrammes) > 0:  
                            ResultatFinal.append("Nombre de programmes: " + str(len(ListeOfProgrammes)))
                            ResultatFinal.append("Nombre de mauvais programmes: " + str(len(ListeOfBadProgramme)))
                            ResultatFinal.append("Nombre de bon programmes: " + str(len(ListeOfGoodProgramme)))
                            ResultatFinal.append("Pourcentage mauvais programmes: " + str(len(ListeOfBadProgramme)/len(ListeOfProgrammes) * 100))
                            ResultatFinal.append("Pourcentage de bon programmes: " + str(len(ListeOfGoodProgramme)/len(ListeOfProgrammes) * 100))
                            
                            
                        chemin4 = currentDirectory + '/FlashFillResults/' + 'Programs1.txt'
                        chemin5 = currentDirectory + '/FlashFillResults/' + 'GoodPrograms1.txt'
                        chemin6 = currentDirectory + '/FlashFillResults/' + 'FakePrograms1.txt'
                        chemin7 = currentDirectory + '/FlashFillResults/' + 'stat1.txt'
                        chemin8 = currentDirectory + '/FlashFillResults/' + 'ErorElements1.txt'
                        
                        with open(chemin4, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin5, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfGoodProgramme))
                            f.write('\n***\n')
                            
                        with open(chemin6, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfBadProgramme))
                            f.write('\n***\n')
                            
                        with open(chemin7, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ResultatFinal))
                            f.write('\n***\n')

                        with open(chemin8, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfFirstEroorElements))
                            f.write('\n***\n')

                    elif numero == '2':
                        ListeDesSorties = []
                        ListeDesEntrees = []
                        ListeOfGoodProgramme = []
                        ListeOfBadProgramme = []
                        ListeDesElementBonneReponse = []
                        ListeOfFirstEroorElements = []
                        ResultatFinal = []
                        
                        with open(CheminBonResultat) as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count = 0
                            for row in  csv_reader:
                                if line_count != 0 and line_count != 1 :
                                    ListeDesElementBonneReponse.append("+++".join(row[:-1]) + '---' + row[-1])
                                    line_count += 1
                                else:
                                    line_count += 1
                        
                        with open(Paths[key][numero]) as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count = 0
                            for row in  csv_reader:
                                if line_count == 0 or line_count == 1:
                                    ListeDesSorties.append("+++".join(row[:-1]) + '---' + row[-1])
                                    line_count += 1
                                else:
                                    ListeDesEntrees.append("+++".join(row[:-1]))
                                    line_count += 1
                                    


                        chemin = currentDirectory +  '/data.txt'
                        chemin2 = currentDirectory + '/dataTest.txt'
                        chemin3 = currentDirectory + '/dataResult.txt'
                        filename = 'dataTest.txt'
                        
                        with open(chemin, 'w') as f:
                            f.write('\n'.join(ListeDesSorties))
                            
                        with open(chemin2, 'w') as f:
                            f.write('\n'.join(ListeDesEntrees))
                        
                        with open(chemin3, 'w') as f:
                            f.write('\n'.join(ListeDesElementBonneReponse))
                            
                        Test = UniformQuickFill()
                        Test.GetClassC()
                        DicoBonneReposese = Test.GetGoodExamples()
                        ListeOfProgrammes = list(Test.GenerateStringProgram3(Test.GetExamples()[0]))
                        for prog in ListeOfProgrammes:
                            spetResultOne = Test.ExecuteOnElements(filename,prog)
                            if spetResultOne == DicoBonneReposese:
                                ListeOfGoodProgramme.append(prog)
                            else:
                                StepBadElement = (DeepDiff(DicoBonneReposese, spetResultOne))["values_changed"]
                                keyToPass,valueToPass = list(StepBadElement.items())[0]
                                keyToPass = keyToPass.replace('root[' ,'',1)
                                last_char_index = keyToPass.rfind("]")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                keyToPass = keyToPass.replace('{' ,'',1)
                                last_char_index = keyToPass.rfind("}")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                valueToPass = str(json.dumps(valueToPass))
                                valueToPass = valueToPass.replace('{' ,'',1)
                                last_char_index = valueToPass.rfind("}")
                                valueToPass = valueToPass[:last_char_index] +  valueToPass[last_char_index+1:]
                                ListeOfFirstEroorElements.append(keyToPass + " : " + valueToPass)
                                ListeOfBadProgramme.append(prog)


                        if len(ListeOfProgrammes) > 0:  
                            ResultatFinal.append("Nombre de programmes: " + str(len(ListeOfProgrammes)))
                            ResultatFinal.append("Nombre de mauvais programmes: " + str(len(ListeOfBadProgramme)))
                            ResultatFinal.append("Nombre de bon programmes: " + str(len(ListeOfGoodProgramme)))
                            ResultatFinal.append("Pourcentage mauvais programmes: " + str(len(ListeOfBadProgramme)/len(ListeOfProgrammes) * 100))
                            ResultatFinal.append("Pourcentage de bon programmes: " + str(len(ListeOfGoodProgramme)/len(ListeOfProgrammes) * 100))
                            
                        chemin4 = currentDirectory + '/FlashFillResults/' + 'Programs2.txt'
                        chemin5 = currentDirectory + '/FlashFillResults/' + 'GoodPrograms2.txt'
                        chemin6 = currentDirectory + '/FlashFillResults/' + 'FakePrograms2.txt'
                        chemin7 = currentDirectory + '/FlashFillResults/' + 'stat2.txt'
                        chemin8 = currentDirectory + '/FlashFillResults/' + 'ErorElements2.txt'
                        
                        with open(chemin4, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin5, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfGoodProgramme))
                            f.write('\n***\n')
                            
                        with open(chemin6, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfBadProgramme))
                            f.write('\n***\n')
                            
                        with open(chemin7, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ResultatFinal))
                            f.write('\n***\n')
                        
                        with open(chemin8, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfFirstEroorElements))
                            f.write('\n***\n')
                        
                    elif numero == '3':
                        ListeDesSorties = []
                        ListeDesEntrees = []
                        ListeOfGoodProgramme = []
                        ListeOfBadProgramme = []
                        ListeDesElementBonneReponse = []
                        ListeOfFirstEroorElements = []
                        ResultatFinal = []                        
                        with open(CheminBonResultat) as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count = 0
                            for row in  csv_reader:
                                if line_count != 0 and line_count != 1 and line_count != 2:
                                    ListeDesElementBonneReponse.append("+++".join(row[:-1]) + '---' + row[-1])
                                    line_count += 1
                                else:
                                    line_count += 1
                        
                        with open(Paths[key][numero]) as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count = 0
                            for row in  csv_reader:
                                if line_count == 0 or line_count == 1 or line_count == 2:
                                    ListeDesSorties.append("+++".join(row[:-1]) + '---' + row[-1])
                                    line_count += 1
                                else:
                                    ListeDesEntrees.append("+++".join(row[:-1]))
                                    line_count += 1
                                    


                        chemin = currentDirectory +  '/data.txt'
                        chemin2 = currentDirectory + '/dataTest.txt'
                        chemin3 = currentDirectory + '/dataResult.txt'
                        filename = 'dataTest.txt'
                        
                        with open(chemin, 'w') as f:
                            f.write('\n'.join(ListeDesSorties))
                            
                        with open(chemin2, 'w') as f:
                            f.write('\n'.join(ListeDesEntrees))
                        
                        with open(chemin3, 'w') as f:
                            f.write('\n'.join(ListeDesElementBonneReponse))
                            
                        Test = UniformQuickFill()
                        Test.GetClassC()
                        DicoBonneReposese = Test.GetGoodExamples()
                        ListeOfProgrammes = list(Test.GenerateStringProgram3(Test.GetExamples()[0]))
                        for prog in ListeOfProgrammes:
                            spetResultOne = Test.ExecuteOnElements(filename,prog)
                            StepBadElement = {}
                            keyToPass = ""
                            valueToPass = ""
                            if spetResultOne == DicoBonneReposese:
                                ListeOfGoodProgramme.append(prog)
                            else:
                                StepBadElement = (DeepDiff(DicoBonneReposese, spetResultOne))["values_changed"]
                                keyToPass,valueToPass = list(StepBadElement.items())[0]
                                keyToPass = keyToPass.replace('root[' ,'',1)
                                last_char_index = keyToPass.rfind("]")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                keyToPass = keyToPass.replace('{' ,'',1)
                                last_char_index = keyToPass.rfind("}")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                valueToPass = str(json.dumps(valueToPass))
                                valueToPass = valueToPass.replace('{' ,'',1)
                                last_char_index = valueToPass.rfind("}")
                                valueToPass = valueToPass[:last_char_index] +  valueToPass[last_char_index+1:]
                                ListeOfFirstEroorElements.append(keyToPass + " : " + valueToPass)
                                ListeOfBadProgramme.append(prog)


                        if len(ListeOfProgrammes) > 0:  
                            ResultatFinal.append("Nombre de programmes: " + str(len(ListeOfProgrammes)))
                            ResultatFinal.append("Nombre de mauvais programmes: " + str(len(ListeOfBadProgramme)))
                            ResultatFinal.append("Nombre de bon programmes: " + str(len(ListeOfGoodProgramme)))
                            ResultatFinal.append("Pourcentage mauvais programmes: " + str(len(ListeOfBadProgramme)/len(ListeOfProgrammes) * 100))
                            ResultatFinal.append("Pourcentage de bon programmes: " + str(len(ListeOfGoodProgramme)/len(ListeOfProgrammes) * 100))
                            
                        
                        chemin4 = currentDirectory + '/FlashFillResults/' + 'Programs3.txt'
                        chemin5 = currentDirectory + '/FlashFillResults/' + 'GoodPrograms3.txt'
                        chemin6 = currentDirectory + '/FlashFillResults/' + 'FakePrograms3.txt'
                        chemin7 = currentDirectory + '/FlashFillResults/' + 'stat3.txt'
                        chemin8 = currentDirectory + '/FlashFillResults/' + 'ErorElements3.txt'
                        
                        with open(chemin4, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin5, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfGoodProgramme))
                            f.write('\n***\n')
                            
                        with open(chemin6, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfBadProgramme))
                            f.write('\n***\n')
                            
                        with open(chemin7, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ResultatFinal))
                            f.write('\n***\n')
                        
                        with open(chemin8, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfFirstEroorElements))
                            f.write('\n***\n')
  
                    elif numero == '4':
                        ListeDesSorties = []
                        ListeDesEntrees = []
                        ListeOfGoodProgramme = []
                        ListeOfBadProgramme = []
                        ListeDesElementBonneReponse = []
                        ListeOfFirstEroorElements = []
                        ResultatFinal = []
                        
                        with open(CheminBonResultat) as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count = 0
                            for row in  csv_reader:
                                if line_count != 0 and line_count != 1 and line_count != 2 and line_count != 3:
                                    ListeDesElementBonneReponse.append("+++".join(row[:-1]) + '---' + row[-1])
                                    line_count += 1
                                else:
                                    line_count += 1
                        
                        with open(Paths[key][numero]) as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count = 0
                            for row in  csv_reader:
                                if line_count == 0 or line_count == 1 or line_count == 2 or line_count == 3:
                                    ListeDesSorties.append("+++".join(row[:-1]) + '---' + row[-1])
                                    line_count += 1
                                else:
                                    ListeDesEntrees.append("+++".join(row[:-1]))
                                    line_count += 1
                                    


                        chemin = currentDirectory +  '/data.txt'
                        chemin2 = currentDirectory + '/dataTest.txt'
                        chemin3 = currentDirectory + '/dataResult.txt'
                        filename = 'dataTest.txt'
                        
                        with open(chemin, 'w') as f:
                            f.write('\n'.join(ListeDesSorties))
                            
                        with open(chemin2, 'w') as f:
                            f.write('\n'.join(ListeDesEntrees))
                        
                        with open(chemin3, 'w') as f:
                            f.write('\n'.join(ListeDesElementBonneReponse))
                            
                        Test = UniformQuickFill()
                        Test.GetClassC()
                        DicoBonneReposese = Test.GetGoodExamples()
                        ListeOfProgrammes = list(Test.GenerateStringProgram3(Test.GetExamples()[0]))
                        for prog in ListeOfProgrammes:
                            spetResultOne = Test.ExecuteOnElements(filename,prog)
                            if spetResultOne == DicoBonneReposese:
                                ListeOfGoodProgramme.append(prog)
                            else:
                                StepBadElement = (DeepDiff(DicoBonneReposese, spetResultOne))["values_changed"]
                                keyToPass,valueToPass = list(StepBadElement.items())[0]
                                keyToPass = keyToPass.replace('root[' ,'',1)
                                last_char_index = keyToPass.rfind("]")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                keyToPass = keyToPass.replace('{' ,'',1)
                                last_char_index = keyToPass.rfind("}")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                valueToPass = str(json.dumps(valueToPass))
                                valueToPass = valueToPass.replace('{' ,'',1)
                                last_char_index = valueToPass.rfind("}")
                                valueToPass = valueToPass[:last_char_index] +  valueToPass[last_char_index+1:]
                                ListeOfFirstEroorElements.append(keyToPass + " : " + valueToPass)
                                ListeOfBadProgramme.append(prog)
                                

                        if len(ListeOfProgrammes) > 0:  
                            ResultatFinal.append("Nombre de programmes: " + str(len(ListeOfProgrammes)))
                            ResultatFinal.append("Nombre de mauvais programmes: " + str(len(ListeOfBadProgramme)))
                            ResultatFinal.append("Nombre de bon programmes: " + str(len(ListeOfGoodProgramme)))
                            ResultatFinal.append("Pourcentage mauvais programmes: " + str(len(ListeOfBadProgramme)/len(ListeOfProgrammes) * 100))
                            ResultatFinal.append("Pourcentage de bon programmes: " + str(len(ListeOfGoodProgramme)/len(ListeOfProgrammes) * 100))
                            
                        
                        chemin4 = currentDirectory + '/FlashFillResults/' + 'Programs4.txt'
                        chemin5 = currentDirectory + '/FlashFillResults/' + 'GoodPrograms4.txt'
                        chemin6 = currentDirectory + '/FlashFillResults/' + 'FakePrograms4.txt'
                        chemin7 = currentDirectory + '/FlashFillResults/' + 'stat4.txt'
                        chemin8 = currentDirectory + '/FlashFillResults/' + 'ErorElements4.txt'
                        
                        with open(chemin4, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin5, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfGoodProgramme))
                            f.write('\n***\n')
                            
                        with open(chemin6, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfBadProgramme))
                            f.write('\n***\n')
                            
                        with open(chemin7, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ResultatFinal))
                            f.write('\n***\n')

                        with open(chemin8, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfFirstEroorElements))
                            f.write('\n***\n')

        elif arg[1] == 'Q':
            
            for key  in Paths:
                DicoBonneReposese = {}
                CheminBonResultat = currentDirectory+'/QuickFillResults/'+key + '/' +key.lower()+'.csv'
                       
                   
                for numero in Paths[key]:
                    
                    print("Debut Cas " + numero + " Benchmark " + key + "\n")
                    if numero == '1':
                        ListeDesSorties = []
                        ListeDesEntrees = []
                        ListeOfGoodProgramme = []
                        ListeOfBadProgramme = []
                        ListeDesElementBonneReponse = []
                        ResultatFinal = []
                        MonElment = []
                        Entrer = []
                        Formuletest= []
                        Test =[]
                        Maformuledecoupe = []
                        NewListeSorties = []
                        TrueEvalvalue = []
                        MonDicoModif = {}
                        NewDico = {}
                        NewVal1 = ""
                        Newval2 = ""
                        Traite1 = []
                        ListeEntreFormeAtraiter = {}
                        MesProgrammes = []
                        ListGoodProgrammes = []
                        ListeBadProgrammes = []
                        ListeOfFirstEroorElements = []
                        Deepcopy1 = []
                        Deepcopy2 = []
                        s = ""
                        s2 = ""
                        s3 = ""
                        ResultatFinal = []
                                                
                        Test = InteractQuickFill()
                        
                        with open(CheminBonResultat) as csv_file:
                            # gestion du fichier resultat contenant les entrees-sorties
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count = 0
                            for row in  csv_reader:
                                if line_count != 0:
                                    #print("voici row : ",row)                                   
                                    ListeDesElementBonneReponse.append("+++".join(row[:-1]) + '---' + row[-1])
                                    line_count += 1
                                else:
                                    line_count += 1

                        with open(Paths[key][numero]) as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=',',quoting=csv.QUOTE_NONE)
                            line_count = 0
                            for row in  csv_reader:

                                if line_count == 0:
                                    for elt in row: 
                                                                                                                                                                         
                                        if "b1***" in elt:                                                 
                                            r = row.index(elt)                                                                           
                                            ListeDesSorties.append(','.join(row[r:]))
                                            
                                    line_count += 1
                                   

                                else:
                               
                                    ListeDesEntrees.append('+++'.join(row[:-1]))
                                    line_count += 1
                                    

                        MonElment = eval(eval(ListeDesSorties[0])[0])
                        Entrer = eval(eval(ListeDesSorties[0])[1])
                        Test = InteractQuickFill()
                        Test.GetClassC()
                        

                        for ett in MonElment:
                            
                            
                            if MonElment[ett] == "ConstStr":
                                    
                                    decoupekeyval = ett.split("***")
                                    Formuletest = "ConstStr(" + decoupekeyval[1] + ")"
                                    
                            else:
                                    decoupekeyval = ett.split("***")
                                    decoupekeyval = decoupekeyval[1].split("+++")
                                    Formuletest = Test.ExpressionConcatenateAbsolute3(Entrer,MonElment[ett],decoupekeyval[1])
                            
                            Maformuledecoupe.append(Formuletest) 
                        
                        
                        
                        
                        for element in ListeDesSorties:
                            TrueEvalvalue = eval(element)
                            MonDicoModif = eval(TrueEvalvalue[0])
                            for element2 in  MonDicoModif:
                                
                                if MonDicoModif[element2] != "ConstStr":
                                    element3 = element2.split("***")
                                    NewVal1 = element3[0]
                                    Newval2 = (element3[1].split("+++"))[0]
                                    NewDico[NewVal1+"***"+Newval2] = MonDicoModif[element2]
                                else:
                                    NewDico[element2] = MonDicoModif[element2]
                            
                            
                            NewListeSorties.append(str((json.dumps(NewDico) , TrueEvalvalue[1] , TrueEvalvalue[2])))
                        
                        ListeDesSorties = NewListeSorties
                        
                        

                        chemin = currentDirectory + '/interactData.txt'
                        chemin2 = currentDirectory +  '/dataQuickFill.txt'
                        chemin3 = currentDirectory + '/dataResultQuickFill.txt'
                        
                        with open(chemin, 'w') as f:
                            f.write('\n'.join(ListeDesSorties))
                            
                        with open(chemin2, 'w') as f:
                            f.write('\n'.join(ListeDesEntrees))
                        
                        with open(chemin3, 'w') as f:
                            f.write('\n'.join(ListeDesElementBonneReponse))


                        s = Test.GetInteractData()[0]
                        s2 = Test.GetTestExemaples()
                        s3 = Test.GetGoodExamples()
                        
                        
                        

                        for elt in s2:
                            Traite1 = {}
                            i = 0
                            for ett in Maformuledecoupe:
                                i=i+1
                                if(ett.startswith("ConstStr")):
                                        Traite1["b"+str(i)] = ett
                                else:
                                    TraiementEntrer = eval(elt)
                                    Traite1["b"+str(i)] = Test.ExecuteFonctionDecoupe(ett,TraiementEntrer)
    

                    
                            ListeEntreFormeAtraiter[elt] = Traite1                       
                    
                        

                        MesProgrammes = list(Test.GenerateStringProgram(s))


              


                        FilteringOutPut = list(s)
                        dicsept1 = {}
                        dicsept2 = {}

                        for elt in FilteringOutPut:
                                dicsept1[json.dumps(elt[1])] = elt[2]
                                dicsept2[json.dumps(elt[1])] = eval(elt[0])


                        if len(dicsept1.keys()) > 0 :
                                MesProgrammes = Test.FilterProgrammesExecution(len(dicsept1.keys()),dicsept1,dicsept2,MesProgrammes)


    

                        for prog in MesProgrammes:
                            Deepcopy1 = copy.deepcopy(s2)
                            Deepcopy2 = copy.deepcopy(ListeEntreFormeAtraiter)
                            StepBadElement = {}
                            keyToPass = ""
                            valueToPass = ""
                            new_string=""
                            last_char_index = 0
                            for elt2 in Deepcopy1:
                                Deepcopy1[elt2] = Test.ExecuteFonction(prog,Deepcopy2[elt2])
                                                           
                            if Deepcopy1 == s3:
                                ListGoodProgrammes.append(prog)
                            else:
                                StepBadElement = (DeepDiff(s3, Deepcopy1))["values_changed"]
                                keyToPass,valueToPass = list(StepBadElement.items())[0]
                                keyToPass = keyToPass.replace('root[' ,'',1)
                                last_char_index = keyToPass.rfind("]")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                keyToPass = keyToPass.replace('{' ,'',1)
                                last_char_index = keyToPass.rfind("}")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                valueToPass = str(json.dumps(valueToPass))
                                valueToPass = valueToPass.replace('{' ,'',1)
                                last_char_index = valueToPass.rfind("}")
                                valueToPass = valueToPass[:last_char_index] +  valueToPass[last_char_index+1:]
                                ListeOfFirstEroorElements.append(keyToPass + " : " + valueToPass)
                                ListeBadProgrammes.append(prog)
                        

                        if len(MesProgrammes) > 0:  
                            ResultatFinal.append("Nombre de programmes: " + str(len(MesProgrammes)))
                            ResultatFinal.append("Nombre de mauvais programmes: " + str(len(ListeBadProgrammes)))
                            ResultatFinal.append("Nombre de bon programmes: " + str(len(ListGoodProgrammes)))
                            ResultatFinal.append("Pourcentage mauvais programmes: " + str(len(ListeBadProgrammes)/len(MesProgrammes) * 100))
                            ResultatFinal.append("Pourcentage de bon programmes: " + str(len(ListGoodProgrammes)/len(MesProgrammes) * 100))
                            
                            
                        chemin4 = currentDirectory + '/QuickFillResults/' + 'Programs1.txt'
                        chemin5 = currentDirectory + '/QuickFillResults/' + 'GoodPrograms1.txt'
                        chemin6 = currentDirectory + '/QuickFillResults/' + 'FakePrograms1.txt'
                        chemin7 = currentDirectory + '/QuickFillResults/' + 'stat1.txt'
                        chemin8 = currentDirectory + '/QuickFillResults/' + 'ErorElements1.txt'
                        
                        with open(chemin4, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(MesProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin5, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListGoodProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin6, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeBadProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin7, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ResultatFinal))
                            f.write('\n***\n')


                        with open(chemin8, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfFirstEroorElements))
                            f.write('\n***\n')
                            
                    

                    elif numero == '2':
                        

                        ListeDesSorties = []
                        ListeDesEntrees = []
                        ListeOfGoodProgramme = []
                        ListeOfBadProgramme = []
                        ListeDesElementBonneReponse = []
                        ResultatFinal = []
                        MonElment = []
                        Entrer = []
                        Formuletest= []
                        Test =[]
                        Maformuledecoupe = []
                        NewListeSorties = []
                        TrueEvalvalue = []
                        MonDicoModif = {}
                        NewDico = {}
                        NewVal1 = ""
                        Newval2 = ""
                        Traite1 = []
                        ListeEntreFormeAtraiter = {}
                        MesProgrammes = []
                        ListGoodProgrammes = []
                        ListeBadProgrammes = []
                        Deepcopy1 = []
                        Deepcopy2 = []
                        ListeOfFirstEroorElements = []
                        s = ""
                        s2 = ""
                        s3 = ""
                        ResultatFinal = []
                                                
                        Test = InteractQuickFill()
                        
                        with open(CheminBonResultat) as csv_file:
                            # gestion du fichier resultat contenant les entrees-sorties
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count = 0
                            for row in  csv_reader:
                                if line_count != 0 and line_count != 1:
                                    #print("voici row : ",row)                                   
                                    ListeDesElementBonneReponse.append("+++".join(row[:-1]) + '---' + row[-1])
                                    line_count += 1
                                else:
                                    line_count += 1

                        with open(Paths[key][numero]) as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=',',quoting=csv.QUOTE_NONE)
                            line_count = 0
                            for row in  csv_reader:

                                if line_count == 0 or line_count == 1:
                                    for elt in row: 
                                                                                                                                                                         
                                        if "b1***" in elt:                                                 
                                            r = row.index(elt)                                                                           
                                            ListeDesSorties.append(','.join(row[r:]))
                                            
                                    line_count += 1
                                   

                                else:
                               
                                    ListeDesEntrees.append('+++'.join(row[:-1]))
                                    line_count += 1
                                    

                        MonElment = eval(eval(ListeDesSorties[0])[0])
                        Entrer = eval(eval(ListeDesSorties[0])[1])
                        Test = InteractQuickFill()
                        Test.GetClassC()
                        

                        for ett in MonElment:
                            
                            
                            if MonElment[ett] == "ConstStr":
                                    
                                    decoupekeyval = ett.split("***")
                                    Formuletest = "ConstStr(" + decoupekeyval[1] + ")"
                                    
                            else:
                                    decoupekeyval = ett.split("***")
                                    decoupekeyval = decoupekeyval[1].split("+++")
                                    Formuletest = Test.ExpressionConcatenateAbsolute3(Entrer,MonElment[ett],decoupekeyval[1])
                            
                            Maformuledecoupe.append(Formuletest) 
                        
                        
                        
                        
                        for element in ListeDesSorties:
                            TrueEvalvalue = eval(element)
                            MonDicoModif = eval(TrueEvalvalue[0])
                            NewDico = {}
                            for element2 in  MonDicoModif:
                                
                                if MonDicoModif[element2] != "ConstStr":
                                    element3 = element2.split("***")
                                    NewVal1 = element3[0]
                                    Newval2 = (element3[1].split("+++"))[0]
                                    NewDico[NewVal1+"***"+Newval2] = MonDicoModif[element2]
                                else:
                                    NewDico[element2] = MonDicoModif[element2]
                            
                            
                            NewListeSorties.append(str((json.dumps(NewDico) , TrueEvalvalue[1] , TrueEvalvalue[2])))
                        
                        ListeDesSorties = NewListeSorties
                        
                        

                        chemin = currentDirectory + '/interactData.txt'
                        chemin2 = currentDirectory +  '/dataQuickFill.txt'
                        chemin3 = currentDirectory + '/dataResultQuickFill.txt'
                        
                        with open(chemin, 'w') as f:
                            f.write('\n'.join(ListeDesSorties))
                            
                        with open(chemin2, 'w') as f:
                            f.write('\n'.join(ListeDesEntrees))
                        
                        with open(chemin3, 'w') as f:
                            f.write('\n'.join(ListeDesElementBonneReponse))


                        s = Test.GetInteractData()[0]
                        s2 = Test.GetTestExemaples()
                        s3 = Test.GetGoodExamples()
                        
                        
                        

                        for elt in s2:
                            Traite1 = {}
                            i = 0
                            for ett in Maformuledecoupe:
                                i=i+1
                                if(ett.startswith("ConstStr")):
                                        Traite1["b"+str(i)] = ett
                                else:
                                    TraiementEntrer = eval(elt)
                                    Traite1["b"+str(i)] = Test.ExecuteFonctionDecoupe(ett,TraiementEntrer)
    

                    
                            ListeEntreFormeAtraiter[elt] = Traite1                       
                    
                        
                        
                        MesProgrammes = list(Test.GenerateStringProgram(s))

                        FilteringOutPut = list(s)
                        dicsept1 = {}
                        dicsept2 = {}

                        for elt in FilteringOutPut:
                                dicsept1[json.dumps(elt[1])] = elt[2]
                                dicsept2[json.dumps(elt[1])] = eval(elt[0])


                        if len(dicsept1.keys()) > 0 :
                                MesProgrammes = Test.FilterProgrammesExecution(len(dicsept1.keys()),dicsept1,dicsept2,MesProgrammes)

                        
                        for prog in MesProgrammes:
                            Deepcopy1 = copy.deepcopy(s2)
                            Deepcopy2 = copy.deepcopy(ListeEntreFormeAtraiter)
                            StepBadElement = {}
                            keyToPass = ""
                            valueToPass = ""
                            new_string=""
                            last_char_index = 0
                            for elt2 in Deepcopy1:
                                Deepcopy1[elt2] = Test.ExecuteFonction(prog,Deepcopy2[elt2])
                                                           
                            if Deepcopy1 == s3:
                                ListGoodProgrammes.append(prog)
                            else:
                                StepBadElement = (DeepDiff(s3, Deepcopy1))["values_changed"]
                                keyToPass,valueToPass = list(StepBadElement.items())[0]
                                keyToPass = keyToPass.replace('root[' ,'',1)
                                last_char_index = keyToPass.rfind("]")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                keyToPass = keyToPass.replace('{' ,'',1)
                                last_char_index = keyToPass.rfind("}")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                valueToPass = str(json.dumps(valueToPass))
                                valueToPass = valueToPass.replace('{' ,'',1)
                                last_char_index = valueToPass.rfind("}")
                                valueToPass = valueToPass[:last_char_index] +  valueToPass[last_char_index+1:]
                                ListeOfFirstEroorElements.append(keyToPass + " : " + valueToPass)
                                ListeBadProgrammes.append(prog)
                        

                        if len(MesProgrammes) > 0:  
                            ResultatFinal.append("Nombre de programmes: " + str(len(MesProgrammes)))
                            ResultatFinal.append("Nombre de mauvais programmes: " + str(len(ListeBadProgrammes)))
                            ResultatFinal.append("Nombre de bon programmes: " + str(len(ListGoodProgrammes)))
                            ResultatFinal.append("Pourcentage mauvais programmes: " + str(len(ListeBadProgrammes)/len(MesProgrammes) * 100))
                            ResultatFinal.append("Pourcentage de bon programmes: " + str(len(ListGoodProgrammes)/len(MesProgrammes) * 100))
                            
                            
                        chemin4 = currentDirectory + '/QuickFillResults/' + 'Programs2.txt'
                        chemin5 = currentDirectory + '/QuickFillResults/' + 'GoodPrograms2.txt'
                        chemin6 = currentDirectory + '/QuickFillResults/' + 'FakePrograms2.txt'
                        chemin7 = currentDirectory + '/QuickFillResults/' + 'stat2.txt'
                        chemin8 = currentDirectory + '/QuickFillResults/' + 'ErorElements2.txt'
                        
                        with open(chemin4, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(MesProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin5, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListGoodProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin6, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeBadProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin7, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ResultatFinal))
                            f.write('\n***\n')
                        

                        with open(chemin8, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfFirstEroorElements))
                            f.write('\n***\n')


                    elif numero == '3':
                        
                        ListeDesSorties = []
                        ListeDesEntrees = []
                        ListeOfGoodProgramme = []
                        ListeOfBadProgramme = []
                        ListeDesElementBonneReponse = []
                        ResultatFinal = []
                        MonElment = []
                        Entrer = []
                        Formuletest= []
                        Test =[]
                        Maformuledecoupe = []
                        NewListeSorties = []
                        TrueEvalvalue = []
                        MonDicoModif = {}
                        NewDico = {}
                        NewVal1 = ""
                        Newval2 = ""
                        Traite1 = []
                        ListeEntreFormeAtraiter = {}
                        MesProgrammes = []
                        ListGoodProgrammes = []
                        ListeBadProgrammes = []
                        ListeOfFirstEroorElements = []
                        Deepcopy1 = []
                        Deepcopy2 = []
                        s = ""
                        s2 = ""
                        s3 = ""
                        ResultatFinal = []
                                                
                        Test = InteractQuickFill()
                        
                        with open(CheminBonResultat) as csv_file:
                            # gestion du fichier resultat contenant les entrees-sorties
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count = 0
                            for row in  csv_reader:
                                if line_count != 0 and line_count != 1 and line_count != 2:
                                    #print("voici row : ",row)                                   
                                    ListeDesElementBonneReponse.append("+++".join(row[:-1]) + '---' + row[-1])
                                    line_count += 1
                                else:
                                    line_count += 1

                        with open(Paths[key][numero]) as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=',',quoting=csv.QUOTE_NONE)
                            line_count = 0
                            for row in  csv_reader:

                                if line_count == 0 or line_count == 1 or line_count == 2:
                                    
                                    for elt in row: 
                                                                                                                                                                         
                                        if "b1***" in elt:                                                 
                                            r = row.index(elt)                                                                           
                                            ListeDesSorties.append(','.join(row[r:]))
                                            
                                    line_count += 1
                                   

                                else:
                               
                                    ListeDesEntrees.append('+++'.join(row[:-1]))
                                    line_count += 1
                                    


                        MonElment = eval(eval(ListeDesSorties[0])[0])
                        Entrer = eval(eval(ListeDesSorties[0])[1])
                        Test = InteractQuickFill()
                        Test.GetClassC()
                        

                        for ett in MonElment:
                            
                            
                            if MonElment[ett] == "ConstStr":
                                    
                                    decoupekeyval = ett.split("***")
                                    Formuletest = "ConstStr(" + decoupekeyval[1] + ")"
                                    
                            else:
                                
                                    decoupekeyval = ett.split("***")
                                    decoupekeyval = decoupekeyval[1].split("+++")
                                    Formuletest = Test.ExpressionConcatenateAbsolute3(Entrer,MonElment[ett],decoupekeyval[1])
                            
                            Maformuledecoupe.append(Formuletest) 
                        
                        
                        
                        
                        for element in ListeDesSorties:
                            TrueEvalvalue = eval(element)
                            MonDicoModif = eval(TrueEvalvalue[0])
                            NewDico = {}
                            for element2 in  MonDicoModif:
                                
                                if MonDicoModif[element2] != "ConstStr":
                                    element3 = element2.split("***")
                                    NewVal1 = element3[0]
                                    Newval2 = (element3[1].split("+++"))[0]
                                    NewDico[NewVal1+"***"+Newval2] = MonDicoModif[element2]
                                else:
                                    NewDico[element2] = MonDicoModif[element2]
                            
                            
                            NewListeSorties.append(str((json.dumps(NewDico) , TrueEvalvalue[1] , TrueEvalvalue[2])))
                        
                        ListeDesSorties = NewListeSorties
                        

                        chemin = currentDirectory + '/interactData.txt'
                        chemin2 = currentDirectory +  '/dataQuickFill.txt'
                        chemin3 = currentDirectory + '/dataResultQuickFill.txt'
                        
                        with open(chemin, 'w') as f:
                            f.write('\n'.join(ListeDesSorties))
                            
                        with open(chemin2, 'w') as f:
                            f.write('\n'.join(ListeDesEntrees))
                        
                        with open(chemin3, 'w') as f:
                            f.write('\n'.join(ListeDesElementBonneReponse))


                        s = Test.GetInteractData()[0]
                        s2 = Test.GetTestExemaples()
                        s3 = Test.GetGoodExamples()
                        
                        
                        

                        for elt in s2:
                            Traite1 = {}
                            i = 0
                            for ett in Maformuledecoupe:
                                i=i+1
                                if(ett.startswith("ConstStr")):
                                        Traite1["b"+str(i)] = ett
                                else:
                                    TraiementEntrer = eval(elt)
                                    Traite1["b"+str(i)] = Test.ExecuteFonctionDecoupe(ett,TraiementEntrer)
    

                    
                            ListeEntreFormeAtraiter[elt] = Traite1                       
                    
                        

                        MesProgrammes = list(Test.GenerateStringProgram(s))
                        FilteringOutPut = list(s)
                        dicsept1 = {}
                        dicsept2 = {}

                        for elt in FilteringOutPut:
                                dicsept1[json.dumps(elt[1])] = elt[2]
                                dicsept2[json.dumps(elt[1])] = eval(elt[0])


                        if len(dicsept1.keys()) > 0 :
                                MesProgrammes = Test.FilterProgrammesExecution(len(dicsept1.keys()),dicsept1,dicsept2,MesProgrammes)
                        
                        for prog in MesProgrammes:
                            Deepcopy1 = copy.deepcopy(s2)
                            Deepcopy2 = copy.deepcopy(ListeEntreFormeAtraiter)
                            StepBadElement = {}
                            keyToPass = ""
                            valueToPass = ""
                            new_string=""
                            last_char_index = 0
                            for elt2 in Deepcopy1:
                                Deepcopy1[elt2] = Test.ExecuteFonction(prog,Deepcopy2[elt2])
                                                           
                            if Deepcopy1 == s3:
                                ListGoodProgrammes.append(prog)
                            else:
                                StepBadElement = (DeepDiff(s3, Deepcopy1))["values_changed"]
                                keyToPass,valueToPass = list(StepBadElement.items())[0]
                                keyToPass = keyToPass.replace('root[' ,'',1)
                                last_char_index = keyToPass.rfind("]")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                keyToPass = keyToPass.replace('{' ,'',1)
                                last_char_index = keyToPass.rfind("}")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                valueToPass = str(json.dumps(valueToPass))
                                valueToPass = valueToPass.replace('{' ,'',1)
                                last_char_index = valueToPass.rfind("}")
                                valueToPass = valueToPass[:last_char_index] +  valueToPass[last_char_index+1:]
                                ListeOfFirstEroorElements.append(keyToPass + " : " + valueToPass)
                                ListeBadProgrammes.append(prog)
                        

                        if len(MesProgrammes) > 0:  
                            ResultatFinal.append("Nombre de programmes: " + str(len(MesProgrammes)))
                            ResultatFinal.append("Nombre de mauvais programmes: " + str(len(ListeBadProgrammes)))
                            ResultatFinal.append("Nombre de bon programmes: " + str(len(ListGoodProgrammes)))
                            ResultatFinal.append("Pourcentage mauvais programmes: " + str(len(ListeBadProgrammes)/len(MesProgrammes) * 100))
                            ResultatFinal.append("Pourcentage de bon programmes: " + str(len(ListGoodProgrammes)/len(MesProgrammes) * 100))
                            
                            
                        chemin4 = currentDirectory + '/QuickFillResults/' + 'Programs3.txt'
                        chemin5 = currentDirectory + '/QuickFillResults/' + 'GoodPrograms3.txt'
                        chemin6 = currentDirectory + '/QuickFillResults/' + 'FakePrograms3.txt'
                        chemin7 = currentDirectory + '/QuickFillResults/' + 'stat3.txt'
                        chemin8 = currentDirectory + '/QuickFillResults/' + 'ErorElements3.txt'
                        
                        with open(chemin4, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(MesProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin5, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListGoodProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin6, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeBadProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin7, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ResultatFinal))
                            f.write('\n***\n')
                        
                        with open(chemin8, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfFirstEroorElements))
                            f.write('\n***\n')


                    elif numero == '4':
                        
                        ListeDesSorties = []
                        ListeDesEntrees = []
                        ListeOfGoodProgramme = []
                        ListeOfBadProgramme = []
                        ListeDesElementBonneReponse = []
                        ResultatFinal = []
                        MonElment = []
                        Entrer = []
                        Formuletest= []
                        Test =[]
                        Maformuledecoupe = []
                        NewListeSorties = []
                        TrueEvalvalue = []
                        MonDicoModif = {}
                        NewDico = {}
                        NewVal1 = ""
                        Newval2 = ""
                        Traite1 = []
                        ListeEntreFormeAtraiter = {}
                        MesProgrammes = []
                        ListGoodProgrammes = []
                        ListeBadProgrammes = []
                        Deepcopy1 = []
                        Deepcopy2 = []
                        ListeOfFirstEroorElements = []
                        s = ""
                        s2 = ""
                        s3 = ""
                        ResultatFinal = []
                                                
                        Test = InteractQuickFill()
                        
                        with open(CheminBonResultat) as csv_file:
                            # gestion du fichier resultat contenant les entrees-sorties
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count = 0
                            for row in  csv_reader:
                                if line_count != 0 and line_count != 1 and line_count != 2 and line_count != 3: 
                                    #print("voici row : ",row)                                   
                                    ListeDesElementBonneReponse.append("+++".join(row[:-1]) + '---' + row[-1])
                                    line_count += 1
                                else:
                                    line_count += 1

                        with open(Paths[key][numero]) as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=',',quoting=csv.QUOTE_NONE)
                            line_count = 0
                            for row in  csv_reader:

                                if line_count == 0 or line_count==1 or line_count==2 or line_count==3: 
                                    for elt in row:                                                                                                                          
                                        if "b1***" in elt:                                                 
                                            r = row.index(elt)                                                                           
                                            ListeDesSorties.append(','.join(row[r:]))
                                            
                                    line_count += 1
                                   

                                else:
                               
                                    ListeDesEntrees.append('+++'.join(row[:-1]))
                                    line_count += 1
                                    
                        

                        MonElment = eval(eval(ListeDesSorties[0])[0])
                        Entrer = eval(eval(ListeDesSorties[0])[1])
                        Test = InteractQuickFill()
                        Test.GetClassC()
                        

                        for ett in MonElment:
                            
                            
                            if MonElment[ett] == "ConstStr":
                                    
                                    decoupekeyval = ett.split("***")
                                    Formuletest = "ConstStr(" + decoupekeyval[1] + ")"
                                    
                            else:
                                    decoupekeyval = ett.split("***")
                                    decoupekeyval = decoupekeyval[1].split("+++")
                                    Formuletest = Test.ExpressionConcatenateAbsolute3(Entrer,MonElment[ett],decoupekeyval[1])
                            
                            Maformuledecoupe.append(Formuletest) 
                        
                        
                        
                        
                        for element in ListeDesSorties:
                            TrueEvalvalue = eval(element)
                            MonDicoModif = eval(TrueEvalvalue[0])
                            NewDico = {}
                            for element2 in  MonDicoModif:
                                
                                if MonDicoModif[element2] != "ConstStr":
                                    element3 = element2.split("***")
                                    NewVal1 = element3[0]
                                    Newval2 = (element3[1].split("+++"))[0]
                                    NewDico[NewVal1+"***"+Newval2] = MonDicoModif[element2]
                                else:
                                    NewDico[element2] = MonDicoModif[element2]
                            
                            
                            NewListeSorties.append(str((json.dumps(NewDico) , TrueEvalvalue[1] , TrueEvalvalue[2])))
                        
                        ListeDesSorties = NewListeSorties
                        
                        

                        chemin = currentDirectory + '/interactData.txt'
                        chemin2 = currentDirectory +  '/dataQuickFill.txt'
                        chemin3 = currentDirectory + '/dataResultQuickFill.txt'
                        
                        with open(chemin, 'w') as f:
                            f.write('\n'.join(ListeDesSorties))
                            
                        with open(chemin2, 'w') as f:
                            f.write('\n'.join(ListeDesEntrees))
                        
                        with open(chemin3, 'w') as f:
                            f.write('\n'.join(ListeDesElementBonneReponse))


                        s = Test.GetInteractData()[0]
                        s2 = Test.GetTestExemaples()
                        s3 = Test.GetGoodExamples()
                        
                        
                        

                        for elt in s2:
                            Traite1 = {}
                            i = 0
                            for ett in Maformuledecoupe:
                                i=i+1
                                if(ett.startswith("ConstStr")):
                                        Traite1["b"+str(i)] = ett
                                else:
                                    TraiementEntrer = eval(elt)
                                    Traite1["b"+str(i)] = Test.ExecuteFonctionDecoupe(ett,TraiementEntrer)
    

                    
                            ListeEntreFormeAtraiter[elt] = Traite1                       
                    
                        
                        
                        MesProgrammes = list(Test.GenerateStringProgram(s))
                        FilteringOutPut = list(s)
                        dicsept1 = {}
                        dicsept2 = {}

                        for elt in FilteringOutPut:
                                dicsept1[json.dumps(elt[1])] = elt[2]
                                dicsept2[json.dumps(elt[1])] = eval(elt[0])


                        if len(dicsept1.keys()) > 0 :
                                MesProgrammes = Test.FilterProgrammesExecution(len(dicsept1.keys()),dicsept1,dicsept2,MesProgrammes)
                        

                        for prog in MesProgrammes:
                            Deepcopy1 = copy.deepcopy(s2)
                            Deepcopy2 = copy.deepcopy(ListeEntreFormeAtraiter)
                            StepBadElement = {}
                            keyToPass = ""
                            valueToPass = ""
                            new_string=""
                            last_char_index = 0
                            for elt2 in Deepcopy1:
                                Deepcopy1[elt2] = Test.ExecuteFonction(prog,Deepcopy2[elt2])
                                                           
                            if Deepcopy1 == s3:
                                ListGoodProgrammes.append(prog)
                            else:
                                StepBadElement = (DeepDiff(s3, Deepcopy1))["values_changed"]
                                keyToPass,valueToPass = list(StepBadElement.items())[0]
                                keyToPass = keyToPass.replace('root[' ,'',1)
                                last_char_index = keyToPass.rfind("]")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                keyToPass = keyToPass.replace('{' ,'',1)
                                last_char_index = keyToPass.rfind("}")
                                keyToPass = keyToPass[:last_char_index] + keyToPass[last_char_index+1:]
                                valueToPass = str(json.dumps(valueToPass))
                                valueToPass = valueToPass.replace('{' ,'',1)
                                last_char_index = valueToPass.rfind("}")
                                valueToPass = valueToPass[:last_char_index] +  valueToPass[last_char_index+1:]
                                ListeOfFirstEroorElements.append(keyToPass + " : " + valueToPass)
                                ListeBadProgrammes.append(prog)
                        

                        if len(MesProgrammes) > 0:  
                            ResultatFinal.append("Nombre de programmes: " + str(len(MesProgrammes)))
                            ResultatFinal.append("Nombre de mauvais programmes: " + str(len(ListeBadProgrammes)))
                            ResultatFinal.append("Nombre de bon programmes: " + str(len(ListGoodProgrammes)))
                            ResultatFinal.append("Pourcentage mauvais programmes: " + str(len(ListeBadProgrammes)/len(MesProgrammes) * 100))
                            ResultatFinal.append("Pourcentage de bon programmes: " + str(len(ListGoodProgrammes)/len(MesProgrammes) * 100))
                            
                            
                        chemin4 = currentDirectory + '/QuickFillResults/' + 'Programs4.txt'
                        chemin5 = currentDirectory + '/QuickFillResults/' + 'GoodPrograms4.txt'
                        chemin6 = currentDirectory + '/QuickFillResults/' + 'FakePrograms4.txt'
                        chemin7 = currentDirectory + '/QuickFillResults/' + 'stat4.txt'
                        chemin8 = currentDirectory + '/QuickFillResults/' + 'ErorElements4.txt'
                        
                        with open(chemin4, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(MesProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin5, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListGoodProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin6, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeBadProgrammes))
                            f.write('\n***\n')
                            
                        with open(chemin7, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ResultatFinal))
                            f.write('\n***\n')
                        
                        with open(chemin8, 'a') as f:
                            f.write(key+'\n')
                            f.write('\n'.join(ListeOfFirstEroorElements))
                            f.write('\n***\n')                        





def LectureStat():
    """ lecture des fichiers stat.txt et sauvagarde dans les listes pour faire les graphiques. """
    arg = sys.argv
    Benchmarks = []
    currentDirectory = os.getcwd()
    if arg[1] == 'F':
        chemin = currentDirectory+'/FlashFillResults'
        with open(chemin,"r", newline=None) as f:
            line_count = 0
            for line in f:
                if line_count == 0:
                    line = line.replace('\n','')
                    line = list(line)
                    line = ''.join(line[1:])
                    Benchmarks.append(int(line))
                    line_count +=1

                elif line_count == 1 :
                    line_count +=1
                    line = line.replace('\n','')
                    line = line.split(':')
                    line = line[-1]
                    line = line.replace(' ','')

                elif line_count == 1 :
                    line_count +=1
                    line = line.replace('\n','')
                    line = line.split(':')
                    line = line[-1]
                    line = line.replace(' ','')
                
                elif line_count == 1 :
                    line_count +=1
                    line = line.replace('\n','')
                    line = line.split(':')
                    line = line[-1]
                    line = line.replace(' ','')
                
                elif line_count == 1 :
                    line_count +=1
                    line = line.replace('\n','')
                    line = line.split(':')
                    line = line[-1]
                    line = line.replace(' ','')

                elif line_count == 1 :
                    line_count +=1
                    line = line.replace('\n','')
                    line = line.split(':')
                    line = line[-1]
                    line = line.replace(' ','')



    """ elif arg[2] == 'Q':
    chemin = currentDirectory+'/QuickFillResults' """





def GraphProduction(l1,l2,l3,l4,Benchmarks):
    """ prends les statistiques que retourne la focntion execution pour en faire des graphiques.
    Ces statistiques sont obtenue par lecture de fichier , l1,l2,l3,l4 representent les donnees recoltees dans
   les fichiers stat.txt"""
    arg = sys.argv
    Benchmarks = []
    currentDirectory = os.getcwd()
    if arg[1] == 'F':
        chemin = currentDirectory+'/FlashFillResults'


    """ elif arg[2] == 'Q':
    chemin = currentDirectory+'/QuickFillResults' """








def main ():
    Chemins = Pretraitement()
    Execution(Chemins)



if __name__ == "__main__":
    main()

