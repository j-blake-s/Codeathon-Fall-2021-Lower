/**
 * Optimizing Stock Profit Price using Greedy Algorithms
 * Copyright 2021 Lalithnarayan C 
 * Section.io
 * Dec. 7 2020
 * 
 */
#include <iostream>
#include <vector>
#include <algorithm>
using std::cin;
using std::cout;
using std:: endl;
using std::vector;
using std::max;
using std::min;

// Returns the maximum profit possible in list of prices
int MaxProfitSol(vector<int> price_list) {
  int min_price = price_list[0];
  int max_profit = price_list[1] - price_list[0];

  for (size_t i = 1; i < price_list.size(); ++i) {
     int poke_card_price_current = price_list[i];
     int tentative_profit = poke_card_price_current - min_price;
     max_profit = max(max_profit, tentative_profit);
     min_price = min(min_price, poke_card_price_current);
  }
  return max_profit;
}

int main(int argc, char * argv[]) {
  vector<int> price_list1;
  price_list1.push_back(1);
  price_list1.push_back(5);
  price_list1.push_back(3);
  price_list1.push_back(2);

  vector<int>pl2;
  pl2.push_back(7);
  pl2.push_back(2);
  pl2.push_back(8);
  pl2.push_back(9);

  vector<int>pl3;
  pl3.push_back(1);
  pl3.push_back(6);
  pl3.push_back(7);
  pl3.push_back(9);

  vector<int>pl4;
  pl4.push_back(9);
  pl4.push_back(7);
  pl4.push_back(4);
  pl4.push_back(1);

  vector<int>pl5;
  pl5.push_back(10);
  pl5.push_back(5);
  pl5.push_back(1);
  pl5.push_back(0);

  vector<int>pl6;
  pl6.push_back(100);
  pl6.push_back(180);
  pl6.push_back(260);
  pl6.push_back(310);
  pl6.push_back(40);
  pl6.push_back(535);
  pl6.push_back(695);

  cout << "List --> Profit($)" << endl;
  int max1 = MaxProfitSol(price_list1);
  int max2 = MaxProfitSol(pl2);
  int max3 = MaxProfitSol(pl3);
  int max4 = MaxProfitSol(pl4);
  int max5 = MaxProfitSol(pl5);
  int max6 = MaxProfitSol(pl6);

  cout << "1.      $" << max1 << endl;
  cout << "2.      $" << max2 << endl;
  cout << "3.      $" << max3 << endl;
  cout << "4.      $" << max4 << endl;
  cout << "5.      $" << max5 << endl;
  cout << "6.      $" << max6 << endl;
  return 0;
}
