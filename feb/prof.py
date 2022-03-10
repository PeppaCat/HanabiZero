#set -ex
export CUDA_DEVICE_ORDER='PCI_BUS_ID'
#export CUDA_VISIBLE_DEVICES=0,1,2
export CUDA_VISIBLE_DEVICES=0,1,2,3
#export CUDA_VISIBLE_DEVICES=3,4,5,6

#python main.py --env KangarooNoFrameskip-v4 --case atari --opr train --seed 0 --num_gpus 3 --num_cpus 60 --force --batch_actor 28 \
#python main.py --env KangarooNoFrameskip-v4 --case atari --opr train --seed 0 --num_gpus 4 --num_cpus 48 --force --batch_actor 42 \
#58
#46/9
# python3 ../main.py --env Hanabi-Small --case hanabi --opr train --seed 10 --num_gpus 4 --num_cpus 110 --force\
#   --cpu_actor 5 --gpu_actor 18 \
#   --p_mcts_num 20\
#   --extra 2022 \
#   --use_priority \
#   --use_max_priority \
#   --revisit_policy_search_rate 0.999 \
#   --amp_type 'torch_amp' \
#   --reanalyze_part 'paper' \
#   --info 'small_resnet' \
#   --actors 15 \
#   --simulations 50 \
#   --batch_size 128 \
#   --val_coeff 0.25 \
#   --td_step 5 \
#   --debug_interval 100 \
#   --lr 0.1 \
#   --decay_rate 0.5 \
#   --decay_step 150000 \
#   --stack 4 \
#   #--debug_batch \

# #revisivt#@wjc current disabled from 0.99

python3 ../main.py --env Hanabi-Full --case hanabi --opr train --seed 10 --num_gpus 4 --num_cpus 100 --force\
  --cpu_actor 5 --gpu_actor 14 \
  --p_mcts_num 20\
  --extra 2022 \
  --use_priority \
  --use_max_priority \
  --revisit_policy_search_rate 0.999 \
  --amp_type 'torch_amp' \
  --reanalyze_part 'paper' \
  --info 'profile' \
  --actors 35 \
  --simulations 50 \
  --batch_size 256 \
  --val_coeff 0.25 \
  --td_step 5 \
  --debug_interval 100 \
  --lr 0.1 \
  --decay_rate 0.1 \
  --decay_step 200000 \
  --stack 1 \
  #--debug_batch \

#revisivt#@wjc current disabled from 0.99
