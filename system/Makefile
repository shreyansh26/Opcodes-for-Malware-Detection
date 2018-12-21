run:
	python preprocess.py
	java -cp ".:./weka.jar" weka.core.converters.CSVLoader final2.csv > final.arff
	javac -cp ".:./weka.jar" evaluate.java
	java -cp ".:./weka.jar" evaluate