void main() {
  //var africanCountries = ['Tanzania', 'Kenya', 'South Africa'];
  //countryinAfrica(africanCountries);
  //addtolist('Uganda', africanCountries);
  //addtolist('Malawi', africanCountries);
  //print('');
  //countryinAfrica(africanCountries);
  //Alternatively use africanCountries.addAll('Malawi','Uganda')
  //print(africanCountries);
  //String company = "Family Bank";
  //print(company.indexOf('l'));
  //printName('Dan');
  //print(chef);
  //int sum = addTwo(8);
  ///print(sum);
  //voting(34);
  const int number = 7;
  print(number);
}

void printName(String name) {
  print(name);
}

void countryinAfrica(list) {
  for (int j = 0; j < list.length; j++) {
    print(list[j]);
  }
}

void addtolist(country, list) {
  list.insert(0, country);
}

var chef = {'name': 'John', 'age': 23, 'chefSpecial': 'choma'};

int addTwo(int a) {
  int b = a + 2;
  return b;
}

void voting(age) {
  if (age >= 18) {
    print("You can vote");
  } else {
    print("Uderage");
  }
}
