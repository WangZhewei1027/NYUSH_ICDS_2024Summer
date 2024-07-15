#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 09:32:47 2019

@author: xg7
"""


class Contacts:
    """
    A class for storing contacts and their phone numbers
    You can refer the textbook: [MIT text], 
    Introduction to Computation and Programming Using Python 
    Chapter 10.3 Figure 10.7
    """

    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
        return

    def _hash(self, name):
        """Convert the name to the label of a bucket
        1. get the unicode of each character in the name[hint: you can use ord()]
        2. compute the remainder of (the_sum_of_all_unicodes/the_number_of_buckets)
        3. return the remainder 
        """
        # insert your code here
        sum = 0
        for c in name:
            sum += ord(c)
        remainder = sum % self.numBuckets
        return remainder

    def addEntry(self, name, phoneNumber):
        """adding the contact information to a bucket. 
        1.find the label of the bucket;
        2.append the (name, phoneNumber) to it.
        """
        # insert your code here
        bucketIndex = self._hash(name)
        self.buckets[bucketIndex].append((name, phoneNumber))

    def getValue(self, name):
        """retrive the contact information
        1. find the bucket where the name is stored
        2. get the phone number of the name in the bucket; 
           if there is collision, take the phone number 
           of the first element in the bucket.
        """
        bucketIndex = self._hash(name)
        bucket = self.buckets[bucketIndex]
        for contact in bucket:
            if contact[0] == name:
                return contact[1]
        return None


# no need to modify the following code
# But please read them carefully so that you will know what you need to do.
if __name__ == "__main__":

    import random

    random.seed(100)

    celebrities = ["John Lennon", "Paul MaCartney", "George Harrison",
                   "Ringo Starr", "Michael Jackson", "Kim Kardashian",
                   "John Snow", "Arya Stark", "Daenerys Targaryen",
                   "Tyrion Lannister", "Jaime Lannister", "Sansa Stark",
                   "Petyr Baelish", "Lord Varys", "Hodor", "Ygritte",
                   "Gilly", "Davos Seaworth", "Cersei Lannister",
                   "Khal Drogo", "Bran Stark", "Theon Greyjoy"]

    # code for generating the my contacts
    # the elements in myContacts are lists of [name, phone numbers]
    myContacts = []
    for name in celebrities:
        phone = random.choice(range(10**5))
        myContacts.append([name, phone])

    print("My contacts are:\n", myContacts)

    # build an instance of Contacts
    numOfBucket = 17
    D = Contacts(numOfBucket)
    for contact in myContacts:
        D.addEntry(contact[0], contact[1])

    # print("\n", "The buckets are:")
    # for hashBucket in D.buckets:
    #     print(' ', hashBucket)
    print("The phone of Tyrion Lannister is ", D.getValue("Tyrion Lannister"))
