from datetime import datetime
import math

print("F24-0518\n")

#Environment Setup ---
WINS = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_terminal(board):
    for a, b, c in WINS:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    if ' ' not in board:
        return 'Draw'
    return None

def evaluate(board, depth):
    # We subtract/add depth so the AI prefers faster wins and slower losses
    winner = check_terminal(board)
    if winner == 'X':
        return 10 - depth
    elif winner == 'O':
        return -10 + depth
    else:
        return 0


# --- 2. The Alpha-Beta Algorithm ---
# Global variables to track statistics during the search
prune_count = 0 

def alpha_beta(board, depth, alpha, beta, is_max, trace_top_level=False):
    global prune_count
    
    terminal_state = check_terminal(board)
    if terminal_state is not None:
        return evaluate(board, depth), None

    best_move = -1

    if is_max:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval_score, _ = alpha_beta(board, depth + 1, alpha, beta, False)
                board[i] = ' ' # Backtrack
                
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = i
                
                alpha = max(alpha, eval_score)
                
                # Tracing requirement for the assignment
                if trace_top_level:
                    print(f"  -> MAX evaluated index {i}: Utility = {eval_score} | α = {alpha}, β = {beta}")
                
                if beta <= alpha:
                    prune_count += 1
                    if trace_top_level:
                        print(f"  [!] ALPHA-BETA CUTOFF triggered by MAX at index {i} (β={beta} <= α={alpha})")
                    break # Prune
        return max_eval, best_move

    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval_score, _ = alpha_beta(board, depth + 1, alpha, beta, True)
                board[i] = ' ' # Backtrack
                
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = i
                
                beta = min(beta, eval_score)
                
                # Tracing requirement for the assignment
                if trace_top_level:
                    print(f"  -> MIN evaluated index {i}: Utility = {eval_score} | α = {alpha}, β = {beta}")
                
                if beta <= alpha:
                    prune_count += 1
                    if trace_top_level:
                        print(f"  [!] ALPHA-BETA CUTOFF triggered by MIN at index {i} (β={beta} <= α={alpha})")
                    break # Prune
        return min_eval, best_move

# The Game Simulation ---
def simulate_game():
    board = [' '] * 9
    current_player = 'X'
    global prune_count
    
    print("=== STARTING SIMULATION: RATIONAL MAX (X) vs RATIONAL MIN (O) ===")
    print_board(board)
    
    while True:
        prune_count = 0
        print(f"--- {current_player}'s Turn ---")
        
        # Determine the best move using Alpha-Beta
        if current_player == 'X':
            # MAX's turn (Starts with alpha=-inf, beta=inf)
            utility, move = alpha_beta(board, 0, -math.inf, math.inf, True, trace_top_level=True)
            print(f"\n[MAX Agent] Chooses index {move} with guaranteed utility: {utility}")
        else:
            # MIN's turn
            utility, move = alpha_beta(board, 0, -math.inf, math.inf, False, trace_top_level=True)
            print(f"\n[MIN Agent] Chooses index {move} with guaranteed utility: {utility}")
            
        print(f"Total branches pruned during this search: {prune_count}")
        
        # Apply the move
        board[move] = current_player
        print_board(board)
        
        # Check for game over
        result = check_terminal(board)
        if result is not None:
            print("=========================================")
            if result == 'Draw':
                print("GAME OVER: It's a perfectly played Draw!")
            else:
                print(f"GAME OVER: Player {result} wins!")
            break
            
        # Swap players
        current_player = 'O' if current_player == 'X' else 'X'


# Run the simulation
simulate_game()