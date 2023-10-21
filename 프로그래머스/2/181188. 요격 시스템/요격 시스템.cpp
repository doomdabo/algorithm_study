#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
int cmp(vector<int>& a, vector<int>& b){
    return a[1]<b[1]; //e를 기준으로 정렬
}
int solution(vector<vector<int>> targets) {
    int answer = 0;
    sort(targets.begin(), targets.end(), cmp);
    int e =0;
    for(auto t:targets){
        if(e<=t[0]){ //마지막으로 요격한 부분이 감당할 수 있는 범위 e보다 현재 미사일의 시작부분 s가 더 크거나 같으면, 새로운 요격을 해야함.
            answer++;//답 추가하고
            e = t[1]; //감당할수 있는 e를 새로 업데이트 해줌
        }
    }
    return answer;
}