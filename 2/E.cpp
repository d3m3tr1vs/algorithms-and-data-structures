#include <iostream>
#include <vector>

using namespace std;

bool good(vector<int>& boxes, int k, int r){
	int n = boxes.size();
	int cows_count = 1;
	int last_box = boxes[0];
	
	for (int i=1;i<n;i++){
		if (boxes[i]-last_box >= r){
			cows_count++;
			last_box = boxes[i];
		}
	}
	
	return (cows_count>=k);
}

main(){
	int n,k,x,m;
	vector <int> a;
	
	cin >> n;
	cin >> k;
	while (cin >> x){
		a.push_back(x);
	}
	int l=0;
	//cout << a[n-1];
	int r=a[n-1]-a[0]+1;
	//cout << l << "," << r <<endl;
	
	while (r-l>1){
		m=(l+r)/2;
		//cout << m <<endl;
		//cout << good(a,k,m)<<endl;
		//cout << l << "," << r <<endl;
		if (good(a,k,m)){
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
