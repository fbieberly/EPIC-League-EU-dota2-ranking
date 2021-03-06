# EPIC League EU/CIS dota2 ranking

I was interested in knowing what the Glicko-2 ranking of the 10 teams competing in the EPIC League tournament during the round-robin group stage. On [liquipedia] the teams are sorted by simple win/loss record.  

[Glicko-2] is the ranking system used for many competitive sports/games--chess, go, Overwatch, etc. 

[liquipedia]: https://liquipedia.net/dota2/EPIC_League/2/Division_1
[Glicko-2]: https://en.wikipedia.org/wiki/Glicko_rating_system

# Results
### At the end of the group stage
```
Glicko-2 ratings (*before* tie-breakers):
     1. VP               1545
     2. NaVi             1529
     3. OG               1527
     4. Liquid           1520
     5. Vikin.gg         1512
     6. Nigma            1504
     7. Secret           1492
     8. Alliance         1470
     9. Just Error       1458
    10. Mudgolems        1434

Glicko-2 ratings (*after* tie-breakers):
     1. VP               1545
     2. NaVi             1529
     3. Secret           1518
     4. Vikin.gg         1512
     5. Liquid           1511
     6. OG               1510
     7. Nigma            1504
     8. Just Error       1474
     9. Alliance         1461
    10. Mudgolems        1426

Liquipedia's win/loss ranking (*after* tie-breakers):
     1.  Virtus.pro      7-2
     2.  Vikin.gg        6-3
     3.  Natus Vincere   6-3
     4.  Team Secret     5-4
     5.  Team Nigma      5-4
     6.  Team Liquid     5-4
     7.  OG              5-4
     8.  Just Error      2-7
     9.  Alliance        2-7
    10. mudgolems        2-7
```

# Comments

All teams started with the same ranking (1500) at the start of the competition.  
I don't really know much about Glicko-2 so, I could be handling the best-of-three series wrong.  
At the end of the group stage, it'll be interesting if any of the bottom two teams (that get kicked out) are ranked in the top 8 by the Glicko-2 algorithm.

# Final thoughts

In the end, the Glicko-2 ratings of the teams at the end of the group stage (including tiebreakers) mostly matched the win/loss+tiebreaker rankings as well. A couple teams are ranked lower in Glicko-2 (Nigma -2, Vikin.gg -2) and a few are ranked higher (Navi +1, Secret +1, OG +1, Liquid +1). While it changes the seeding of the tournament bracket a little, it does not change who is in the upper and lower brackets. By the end of the tiebreakers, the last two teams which are eliminated prior to the bracket at the same in the two ranking systems.
