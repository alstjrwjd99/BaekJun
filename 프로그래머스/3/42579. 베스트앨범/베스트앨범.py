from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_by_play = defaultdict(int)
    genre_by_idx = defaultdict(list)
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_by_play[genre] += play
        genre_by_idx[genre].append((play,idx))
        
    genre_ranking = sorted(genre_by_play.keys(), key=lambda g: genre_by_play[g], reverse=True)
    
    for genre in genre_ranking:
        target_list = sorted(genre_by_idx[genre], key=lambda x : (-x[0],x[1]))
        answer.append(target_list[0][1])
        if len(target_list) > 1:
            answer.append(target_list[1][1])
            
    return answer