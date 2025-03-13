# hadoop-mapreduce-wordcount
Digitalskola hadoop homework

# Hadoop MapReduce Word Count

Proyek ini adalah implementasi sederhana dari **MapReduce** menggunakan **Hadoop Streaming** untuk menghitung frekuensi kata (word count) dalam teks **Pembukaan UUD 1945**.

## File yang Disertakan
1. **`main.ipynb`**: File notebook yang berisi seluruh proses pengerjaan.
2. **`mapper.py`**: Script Python untuk mapper.
3. **`reducer.py`**: Script Python untuk reducer.
4. **`wordcount.txt`**: File input teks (Pembukaan UUD 1945).
5. **`output_word_count.txt`**: File output hasil MapReduce (word count).

## Cara Menjalankan Proyek
1. **Persiapan**:
   - Pastikan Hadoop sudah terinstal dan berjalan.
   - Upload file `wordcount.txt` ke HDFS:
     ```bash
     hdfs dfs -put wordcount.txt /word_count/wordcount.txt
     ```

2. **Jalankan MapReduce Job**:
   - Gunakan Hadoop Streaming untuk menjalankan MapReduce:
     ```bash
     hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar \
       -input /word_count/wordcount.txt \
       -output /word_count/output \
       -mapper "python mapper.py" \
       -reducer "python reducer.py"
     ```

3. **Ambil Output**:
   - Copy output dari HDFS ke lokal:
     ```bash
     hdfs dfs -copyToLocal /word_count/output/part-00000 output_word_count.txt
     ```

4. **Lihat Hasil**:
   - Output akan disimpan di `output_word_count.txt`.

## Hasil Output
Output akan berisi daftar kata beserta frekuensinya, seperti:
