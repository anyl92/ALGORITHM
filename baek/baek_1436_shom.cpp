#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int N = -1;
	
	cin >> N;
	int k = -1;
	int tmp_int = 666;
	vector<int> cnt_list;
	bool stop = false;

	while (k < 10000001) {
		string tmp_str = to_string(tmp_int);
		for (int i = 0; i < (tmp_str.length() - 2); i++) {
			bool flag = true;
			for (int j = 0; j < 3; j++) {
				if (tmp_str[i + j] != '6') {
					flag = false;
					break;
				};
			};
			if (flag) {
				int idx = cnt_list.size();
				//cout << idx << endl;
				if (idx > 0) {
					cout << cnt_list.back() << endl;
					cout << tmp_int << endl;
					if (cnt_list.back() != tmp_int) {
						cnt_list.emplace_back(tmp_int);
					}
				}
				else {
					cnt_list.emplace_back(tmp_int);
				};
				//if (cnt_list.size() > 1 && cnt_list[cnt_list.size() - 2] == tmp_int) {
				//	cout << cnt_list.size() << endl;
				//	cnt_list.pop_back();
				//}
				
				k++;
			};
			if (k == N - 1) {
				stop = true;
				break;
			};
		};
		if (stop) {
			cout << cnt_list[k];
			cout << endl;
			break;
		};
		tmp_int++;
	};
};