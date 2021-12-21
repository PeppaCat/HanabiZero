#set -ex
export CUDA_DEVICE_ORDER='PCI_BUS_ID'
#export CUDA_VISIBLE_DEVICES=0,1,2
export CUDA_VISIBLE_DEVICES=0,1,2,3
#export CUDA_VISIBLE_DEVICES=3,4,5,6

#python main.py --env KangarooNoFrameskip-v4 --case atari --opr train --seed 0 --num_gpus 3 --num_cpus 60 --force --batch_actor 28 \
#python main.py --env KangarooNoFrameskip-v4 --case atari --opr train --seed 0 --num_gpus 4 --num_cpus 48 --force --batch_actor 42 \
#58
#46/9
python3 ../main.py --env Hanabi-Full --case hanabi --opr train --seed 10 --num_gpus 4 --num_cpus 50 --force --batch_actor 5\
  --p_mcts_num 8\
  --extra full_2p_no_reanal \
  --use_priority \
  --use_max_priority \
  --revisit_policy_search_rate 0.99 \
  --amp_type 'torch_amp' \
  --reanalyze_part 'none' \
  --info 'full_share_confirm' \
  --actors 20 \
  --simulations 50 \
  --batch_size 128 \
  --val_coeff 1 \
  --td_step 8 \
  --debug_interval 100 \
  --lr 0.001 \
  --stack 1

  #--debug_batch \

#revisivt#@wjc current disabled from 0.99
