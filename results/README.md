# Leaderboards of top 10k osu! standard players, grouped by mods
Ever wondered who the best NoMod players are?
Ever wondered who the best at AR11 are?
I compiled data from the best 10 000 players, grouped their best scores by mods, and used this to create leaderboards.
Each leaderboard only takes the scores of each player fitting the criteria (as listed below) into account, which are then weighted and summed up, as in the regular performance ranking system.
This allows comparisons of player pp's on a mod-by-mod basis.

## Mod Leaderboards
The following table shows what mod combinations each table uses.
:heavy_multiplication_x: means that that mod is not allowed to be active.
:heavy_check_mark: means that that mod must be active.
A blank space means that whether the mod is active or not does not matter.

| Mod combination |  HR  |  DT  |  HD  |  FL  |  EZ  |  HT  |  SD  |  PF  |  SO  |  NF  |  NC  |
| --------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| [AnyMod](AnyMod.markdown) |  |  |  |  |  |  |  |  |
| [NoMod](NoMod.markdown) | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: |  |  |  |  |  |
| [HR only](HR only.markdown) | :heavy_check_mark: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: |  |  |  |  |  |
| [DT only](DT only.markdown) | :heavy_multiplication_x: | :heavy_check_mark: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: |  |  |  |  |  |
| [HD only](HD only.markdown) | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_check_mark: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: |  |  |  |  |  |
| [FL only](FL only.markdown) | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_check_mark: | :heavy_multiplication_x: | :heavy_multiplication_x: |  |  |  |  |  |
| [EZ only](EZ only.markdown) | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_check_mark: | :heavy_multiplication_x: |  |  |  |  |  |
| [HT only](HT only.markdown) | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_check_mark: |  |  |  |  |  |
| [NC only](NC only.markdown) | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: |  |  |  |  | :heavy_check_mark: |
| [HR + others](HR + others.markdown) | :heavy_check_mark: |  |  |  |  |  |  |  |  |  |  |
| [DT + others](DT + others.markdown) |  | :heavy_check_mark: |  |  |  |  |  |  |  |  |  |
| [HD + others](HD + others.markdown) |  |  | :heavy_check_mark: |  |  |  |  |  |  |  |  |
| [FL + others](FL + others.markdown) |  |  |  | :heavy_check_mark: |  |  |  |  |  |  |  |
| [EZ + others](EZ + others.markdown) |  |  |  |  | :heavy_check_mark: |  |  |  |  |  |  |
| [HT + others](HT + others.markdown) |  |  |  |  |  | :heavy_check_mark: |  |  |  |  |  |
| [NF + others](NF + others.markdown) |  |  |  |  |  |  |  |  |  | :heavy_check_mark: |  |
| [DTHR(HD)](DTHR(HD).markdown) | :heavy_check_mark: | :heavy_check_mark: |  | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: |  |  |  |  |  |
| [HDHR only](HDHR only.markdown) | :heavy_check_mark: | :heavy_multiplication_x: | :heavy_check_mark: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: |  |  |  |  |  |
| [NoMod or HD](NoMod or HD.markdown) | :heavy_multiplication_x: | :heavy_multiplication_x: |  | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: |  |  |  |  |  |
| [!DT !HR](!DT !HR.markdown) | :heavy_multiplication_x: | :heavy_multiplication_x: |  |  |  |  |  |  |  |  |  |
| [FullMod](FullMod.markdown) | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_multiplication_x: | :heavy_multiplication_x: |  |  |  |  |  |

## Dataset
The dataset was created using the 50 best scores of every player with rank 10 000 or better.
Bonus pp is not calculated.
The default [exponential decay weighting](https://osu.ppy.sh/wiki/Performance_Points#Weightage_system) with the same decay rate is used.
The difference between the value on the AnyMod leaderboard and the real pp results from the lack of bonus pp and the lack of scores that are not in the top 50 best scores of a player.
Note that due to the weighting, people who have a bit of everything in their top performances will not rank highly in the more restrictive mod leaderboards.
Also, since only the top 50 performances of every player are considered, people such as hvick225 who have some good NoMod scores will not appear in the NoMod leaderboards because they simply don't appear in their top 50 performances.

Collection period of the top 10 000 players was done on 25-07-2015 11:00 UTC.
Collection period of their corresponding scores was done from roughly 25-07-2015 21:30 UTC to 26-07-2015 00:30 UTC.
