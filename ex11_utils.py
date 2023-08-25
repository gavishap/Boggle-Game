from typing import List, Tuple, Iterable, Optional

Board = List[List[str]]
Path = List[Tuple[int, int]]


def is_valid_path(board, path, words) :
    word = ""
    i=0
    for coord in path:
        x=coord[0]
        y=coord[1]
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return None
        word += board[x][y]
        i+=1
    if word in words:
        return word
    return None


def find_length_n_paths(n, board, words):
    def dfs(x, y, curr_word, visited):
        if len(curr_word) == n:
            if curr_word in words:
                paths.append(visited.copy())
            return
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y, len(board), len(board[0])) and (new_x, new_y) not in visited:
                visited.append((new_x, new_y))
                dfs(new_x, new_y, curr_word + board[new_x][new_y], visited)
                visited.pop()
    
    paths = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            dfs(i, j, board[i][j], [(i, j)])
    return paths




def find_length_n_words(n, board, words):
    def dfs(x, y, curr_word, visited):
        if len(curr_word) == n:
            if curr_word in words:
                valid_paths.append(visited[:])
            return
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y, len(board), len(board[0])):
                if (new_x, new_y) not in visited:
                    curr_word += board[new_x][new_y]
                    visited.append((new_x, new_y))
                    dfs(new_x, new_y, curr_word, visited)
                    visited.pop()
                    curr_word = curr_word[:-1]

    valid_paths = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            dfs(i, j, "", [(i, j)])
    return valid_paths



def find_words(n, board, words) :
    n_words = set()
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            find_possible_words(n, board, visited, (i, j), "", words, n_words)
    return list(n_words)

def find_possible_words(n, board, visited, curr, curr_word, words, n_words) :
    if len(curr_word) == n:
        if curr_word in words:
            n_words.add(curr_word)
        return
    x, y = curr
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(new_x, new_y, len(board), len(board[0])) and not visited[new_x][new_y]:
            visited[new_x][new_y] = True
            find_possible_words(n, board, visited, (new_x, new_y), curr_word + board[new_x][new_y], words, n_words)
            visited[new_x][new_y] = False

def is_valid_move(x, y, rows, cols) :
    return 0 <= x < rows and 0 <= y < cols






def max_score_paths(board, words):
    max_score = 0
    max_paths = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                curr_path = []
                curr_score = 0
                dfs(board, i, j, dx, dy, curr_path, curr_score, words, max_score, max_paths)
    return max_paths

def dfs(board, x, y, dx, dy, curr_path, curr_score, words, max_score, max_paths) :
    curr_path.append((x, y))
    curr_word = "".join([board[x][y] for x, y in curr_path])
    if curr_word in words:
        curr_score += len(curr_word) ** 2
        if curr_score > max_score:
            max_score = curr_score
            max_paths.clear()
            max_paths.append(curr_path.copy())
        elif curr_score == max_score:
            max_paths.append(curr_path.copy())
    if is_valid_move(x + dx, y + dy, len(board), len(board[0])):
        dfs(board, x + dx, y + dy, dx, dy, curr_path, curr_score, words, max_score, max_paths)
    curr_path.pop()





