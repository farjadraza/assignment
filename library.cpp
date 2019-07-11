#include<iostream>
#include<string.h>
using namespace std;
int a,b,id[5],cost[5],i=0,g=2;
string title[5],aut[5],name;
char choice;
	void intro()
	{
		cout<<"*********** LIBRARY BOOK RECORD SYSTEM ***********"<<endl<<endl;
		cout<<"press 1 to enter a book record"<<endl;
		cout<<"press 2 to display all records of books available in library"<<endl;
		cout<<"press 3 to search books by author name"<<endl;
		cout<<"press 4 to count total books in library"<<endl;
		cout<<"press 5 to exit from the system"<<endl;
    }
    
    void book_record()
    {
    	i=i+1;
    	cout<<"*** enter the details of book ***"<<endl<<endl;
    	cout<<"enter the book id: ";
    	cin>>id[i];
    	cout<<"enter the book title: ";
    	cin>>title[i];
    	cout<<"enter the name of author: ";
    	cin>>aut[i];
    	cout<<"enter the cost of book: ";
    	cin>>cost[i];
	}
	
	void display_records()
	{
		for (b=1;b<=i;b++)
		{
			cout<<"book id "<<id[b]<<endl;
			cout<<"book title "<<title[b]<<endl;
			cout<<"Author name "<<aut[b]<<endl;
			cout<<"cost of book "<<cost[b]<<endl;
			cout<<endl;
		}
	}
	
	void total_books()
	{
		cout<<"the total number of books in library are "<<i<<endl;
	}
	
	void search()
	{
		cout<<"enter the name of author: ";
		cin>>name;
		for (int s=1;s<=5;s++)
		{
			if(name.compare(aut[s])==0)
			{
			cout<<"book id: "<<id[s]<<endl;
			cout<<"book title: "<<title[s]<<endl;
			cout<<"Author name: "<<aut[s]<<endl;
			cout<<"cost of book: "<<cost[s]<<endl;	
			}
		}
	}
int main()
{
	do
	{
		intro();
		cout<<"enter the choice ";
		cin>>a;
		cout<<endl;
		switch (a)
		{
			case 1:do
			{
			book_record();
			cout<<"/n do you want to continue please press Y or y ";
	    	cin>>choice;
			cout<<endl;
			}
			while(choice=='y'|| choice=='Y');
			break;
			case 2:display_records();break;
			case 3:search();break;
			case 4:total_books();break;
			case 5:break;
			default:cout<<"sorry wrong input"; 
		}
		
	}while(a!=5);
}
	
	

