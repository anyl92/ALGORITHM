function solution(board, moves) {
    let answer = 0;
    let result_list = [];
    for (var i=0; i<moves.length; i++) {
        let cur = moves[i] - 1
        for (var j=0; j<board.length; j++) {
            if (board[j][cur]) {
                result_list.push(board[j][cur])
                board[j][cur] = 0
                break
            }
        }
        let last_idx = result_list.length - 1
        if (result_list.length > 1 && result_list[last_idx] == result_list[last_idx-1]) {
            result_list.pop()
            result_list.pop()
            answer += 2
        }
        // let last_idx = result_list.length - 1
        // while (result_list[last_idx] == result_list[last_idx-1]) {
        //     result_list.pop()
        //     result_list.pop()
        //     answer += 2
        //     if (result_list.length < 1) {
        //         break
        //     }
        //     last_idx = result_list.length -1
        // }
    }
    return answer;
}

console.log(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [2, 2, 2]))