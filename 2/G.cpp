#include <iostream>
#include <vector>

using namespace std;

bool good(int x, vector<int>& a, int k){
	if (x==0){
		return false;
	}
	int cnt=0;
	int n = a.size();
	for (int i=0;i<n;i++){
		cnt=cnt+a[i]/x;
	}
	return cnt>=k;
}

main(){
	int n,k,m,x;
	vector <int> a;
	
	cin >> n;
	cin >> k;
	while (cin >> x){
		a.push_back(x);
	}
	
	int l=0;
	int r=10000000+1;
	
	//cout << r << endl;
	
	for (int i=0;i<100;i++){
		m=(l+r)/2;
		if (good(m,a,k)){
			l=m;
		}
		else{
			r=m;
		}
	}
	
	cout << l;
	
	//cout << n << endl;
	//cout << k << endl;
	//for (int i=0; i<n;i++){
	//	cout << a[i] << " ";
	//}
}


