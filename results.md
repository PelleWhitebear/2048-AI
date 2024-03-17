
### Results with depth = 3, and AI heurtic funciton. 
Best weights array: [ 5.33652116  1.2279279  -2.29087275  3.11583057]
Best AIWeights instance: AIWeights(w_open=5.336521160788287, w_edge=1.227927904779254, w_mono=-2.2908727512303084, w_merge=3.115830573443014)
Best score (highest tile achieved): 4096

### Results with depth = 3, and expect_ai heurtic function
Best weights array: [-0.9244403  -0.19722614  0.6175636   2.22559781 -0.75579447]
Best AIWeights instance: AIWeights(w_open=-0.9244402976980419, w_edge=-0.19722614221772916, w_mono=0.6175635979241895, w_merge=2.2255978147452407, w_empty=-0.7557944679514585)
Best score (highest tile achieved): 4096

### Results with depth = 2, and expect_ai heurtic function, and new objective functioin
Best weights array: [ 32.68369402  -2.83239528   3.87983126  10.67103418 -22.74928242]
Best AIWeights instance: AIWeights(w_open=32.683694024472544, w_edge=-2.8323952817780897, w_mono=3.879831259907803, w_merge=10.671034176282877, w_empty=-22.74928242356081)
Best score (highest tile achieved): 27656192 

### rsults with dept = 3, snake ai heurtic. max tile eval
Best weights array: [-2.61482931 -0.15777518 -0.05735801  0.58373137 -2.04521469]
Best AIWeights instance: AIWeights(w_open=-2.614829307400277, w_edge=-0.15777518003719804, w_mono=-0.057358006532466754, w_merge=0.5837313703799336, w_empty=-2.045214693654272)
Best score (highest tile achieved): 4096
{1024: 9, 4096: 1, 512: 3, 2048: 7}

#### Same but on total sum instead. 
Optimizing: 100%|████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [51:26<00:00, 30.86s/iter] 
Best weights array: [ 0.79321068 -1.81229635 -2.82661222  2.58802469  2.81613126]
Best AIWeights instance: AIWeights(w_open=0.7932106804266141, w_edge=-1.8122963456784016, w_mono=-2.826612224485512, w_merge=2.5880246946301564, w_empty=2.816131262925884)
Best score (highest tile achieved): 7200
{512: 5, 2048: 11, 4096: 1, 1024: 3}

### sarch depth 1.
Best weights array: [12.33147924  4.60545762 -5.91448258  6.20115675  0.98227981]
Best AIWeights instance: AIWeights(w_open=12.331479240047372, w_edge=4.605457624021539, w_mono=-5.914482583951802, w_merge=6.201156747582119, w_empty=0.982279805907757)
Best score (highest tile achieved): 8016
{4096: 3, 2048: 12, 1024: 5}