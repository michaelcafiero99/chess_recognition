import chess
import chess.engine
import asyncio


#basically, we need to generate this board string based on the results of the computer vision model
#starts at 8th rank. Lowercase is black, uppercase is white
# "1" means 1 empty square, 2 means 2 empty...ect
board = chess.Board("r1bqkb1r/pppp2pp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
print(board)
engine = chess.engine.SimpleEngine.popen_uci("stockfish")
info = engine.analyse(board, chess.engine.Limit(time=0.1))
print("Score:", info["score"])
chess.engine.AnalysisResult()
print(chess.engine.BestMove)
best_move = engine.play(board, chess.engine.Limit(time=0.5))
print(best_move)
engine.quit()