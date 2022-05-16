python3 DB_PreInput.py
python3 DB_jieba.py
hadoop fs -mkdir -p /user/hduser_/ipt_1
hadoop fs -mkdir -p /user/hduser_/ipt_2
hadoop fs -mkdir -p /user/hduser_/ipt_3
hadoop fs -put ./DB_SegInput_film2/*0.txt /user/hduser_/ipt_1
hadoop fs -put ./DB_SegInput_film2/*1.txt /user/hduser_/ipt_1
hadoop fs -put ./DB_SegInput_film2/*2.txt /user/hduser_/ipt_1
hadoop fs -put ./DB_SegInput_film2/*3.txt /user/hduser_/ipt_2
hadoop fs -put ./DB_SegInput_film2/*4.txt /user/hduser_/ipt_2
hadoop fs -put ./DB_SegInput_film2/*5.txt /user/hduser_/ipt_2
hadoop fs -put ./DB_SegInput_film2/*6.txt /user/hduser_/ipt_3
hadoop fs -put ./DB_SegInput_film2/*7.txt /user/hduser_/ipt_3
hadoop fs -put ./DB_SegInput_film2/*8.txt /user/hduser_/ipt_3
hadoop fs -put ./DB_SegInput_film2/*9.txt /user/hduser_/ipt_3

hadoop fs -rm -r /user/hduser_/opt2_TokenPosition_1
hadoop jar /home/hduser_/hadoop-3.3.2/share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar \
	-input /user/hduser_/ipt_1 \
	-output /user/hduser_/opt2_TokenPosition_1\
	-mapper "python3 ./SearchEngine/TokenPosition_Mapper.py" \
	-reducer "python3 ./SearchEngine/TokenPosition_Reducer.py" \
	-file ./SearchEngine/TokenPosition_Mapper.py \
    -file ./SearchEngine/TokenPosition_Reducer.py

hadoop fs -rm -r /user/hduser_/opt2_TokenPosition_2
hadoop jar /home/hduser_/hadoop-3.3.2/share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar \
	-input /user/hduser_/ipt_2 \
	-output /user/hduser_/opt2_TokenPosition_2\
	-mapper "python3 ./SearchEngine/TokenPosition_Mapper.py" \
	-reducer "python3 ./SearchEngine/TokenPosition_Reducer.py" \
	-file ./SearchEngine/TokenPosition_Mapper.py \
    -file ./SearchEngine/TokenPosition_Reducer.py

hadoop fs -rm -r /user/hduser_/opt2_TokenPosition_3
hadoop jar /home/hduser_/hadoop-3.3.2/share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar \
	-input /user/hduser_/ipt_3 \
	-output /user/hduser_/opt2_TokenPosition_3\
	-mapper "python3 ./SearchEngine/TokenPosition_Mapper.py" \
	-reducer "python3 ./SearchEngine/TokenPosition_Reducer.py" \
	-file ./SearchEngine/TokenPosition_Mapper.py \
    -file ./SearchEngine/TokenPosition_Reducer.py