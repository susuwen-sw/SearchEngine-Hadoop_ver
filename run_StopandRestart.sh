cd hadoop-3.3.2
stop-all.sh
sudo rm -rf logs
sudo rm -rf /data/hadoop/data
sudo rm -rf /data/hadoop/name
sudo rm -rf /data/hadoop/tmp
sudo mkdir -p logs
sudo mkdir -p /data/hadoop/data
sudo mkdir -p /data/hadoop/name
sudo mkdir -p /data/hadoop/tmp
sudo chown -R hduser_:hadoop_ logs
sudo chown -R hduser_:hadoop_ /data/hadoop/data
sudo chown -R hduser_:hadoop_ /data/hadoop/name
sudo chown -R hduser_:hadoop_ /data/hadoop/tmp
hdfs namenode -format
start-all.sh