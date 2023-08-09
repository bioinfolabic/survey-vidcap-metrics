python generate_tsv_2.py --net res101 --dataset vg  --out data_video_scan.txt

python convert_data.py --imgid_list videos_ids.txt --input_file data_video_scan.txt --output_file data_video_scan.npy
