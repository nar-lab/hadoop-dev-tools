sqoop  import  --connect jdbc:oracle:thin:@localhost:1521:orcl  --username ORAMLUSER  --password-file /user/oracle/.password  -m 1  --table S  --target-dir /user/oracle/berka/S  --delete-target-dir  --as-textfile  --fetch-size 1000  --lines-terminated-by '\n'  --fields-terminated-by '|'  --input-null-string ''  --input-null-non-string ''  --mapreduce-job-name sqoop_job_S              