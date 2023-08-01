#include <iostream>
#include <vector>

using namespace std;

int Check(vector<string>& board, int x, int y){
    int count1 = 0, count2 = 0;
    for(int i = x; i < x + 8; ++i) {
        for(int j = y; j < y + 8; ++j) {
            if((i+j) % 2 == 0){
                if(board[i][j] != 'W') count1++;
                if(board[i][j] != 'B') count2++;
            }
            else {
                if(board[i][j] != 'B') count1++;
                if(board[i][j] != 'W') count2++;
            }
        }
    }
    return min(count1, count2);
}

int main(){
    int N, M;
    cin >> N >> M;
    vector<string> board(N);
    for(int i = 0; i <= N; ++i) {
        cin >> board[i];
    }
    int minPart = 987654321;
    for (int i = 0; i <= N - 8; ++i){
        for (int j = 0; j <= M - 8; ++j){
            int paint = Check(board, i ,j);
            minPart = min(minPart, paint);
        }
    }

    cout << minPart << endl;
    return 0;
}