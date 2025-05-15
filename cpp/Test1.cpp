//
// Created by lks on 2025/5/15.
//
#include <iostream>
#include <string>
#include <utility>

using namespace std;

/**
 * public class外部和内部可以访问，子类可以继承访问，例如calssCase.para1
 * private class内部可以访问，外部不可以访问，子类可以继承
 * protected class内部可以访问，外部不可以访问，子类不可以继承访问
 * 成员属性一般设置成私有化，访问或者获取通过getter/setter控制读取权限
 */
class Student {
public:

	int a = 0;
	int b = 0;
	/* 构造函数和析构函数 */
	Student();
	explicit Student(string name) {
		this->name = std::move(name);
	}

	/* 拷贝构造 */
	Student(const Student &student) {
		this->name = student.name;
	}

	/* 初始化列表 */
	Student(const int a, const int b):	a(a), b(b) {

	}

	~Student();

	void showStudent() const {
		cout << "Name: " << name << " id" << id << endl;
	}

	void setName(const string &name) {
		this->name = name;
	}

	void setId(const int id) {
		this->id = id;
	}

	string getName() const {
		return this->name;
	}

	int getId() const {
		return this->id;
	}

	void setTest(const int test) {
		this->test = test;
	}

	int getTest() const {
		return this->test;
	}

private:
	string name;
	int id = 0;
	int password = 0;
	string name_;

	int getPassword() const {
		return password;
	}

	void setPassword(int password) {
		this->password = password;
	}

protected:
	int test = 0;
};

void swap(int &a, int &b) noexcept {
	const int temp = a;
	a = b;
	b = temp;
}

/* 默认参数和占位参数 */
void test1(const int &a = 10, int = 20) {
	cout << a << endl;
}

void test1(int *a, const int b, const int c) {
	*a = b + c;
	cout << a << endl;
}

int main() {
	Student s;

	Student s1;
	s1.setTest(100);
	cout << s1.getTest() << endl;
}
