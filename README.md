<h1 align="center">  GUI Based Library Management System designed using PyQt5 </h1>

This project is written as a thorough guide for making a graphical user interface for Library Management System. The code is highly based on PyQt5. PyQt5 is cross-platform GUI toolkit, a set of python bindings for Qt v5. Any interactive desktop application can be developed with so much ease because of the tools and simplicity provided by this library. 

# Install

### Clone the repository:

          git clone https://github.com/Lizahh/GUI-Based-Library-Management-System-desinged-with-PyQt5

### Install the requiements:
  
          pip3 install -r requirements.txt
      
# Description
 
  * The project has 8 python (.py files) modules in which **project.py** file is the main file. The user interface is designed by dragging and dropping the widgets from PyQt5's designer which is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in
  * After creating the user interface, 4 .ui files (main_windows.ui, add_book_dialog.ui, edit_dialog.ui and delete.ui) are generated
  *  The user interface (.ui) files are converted to the python (.py) files (main_window.py, add_book_dialog.py, edit_dialog.py, and delete_dialog.py) using pyuic5-tool 0.0.1 which is the dev tool to make the conversion of .ui PyQt5 Designer's files to .py files by making an instance of the included class and calling the convert.ui method at the entry point of the code. 
  * The main UI classes of all these 4 files are imported to the 'project.py' file which has the complete functionality of application
  * The application interface has one main windows and 3 dialog windows: one dialog window for adding a new book, one for editing book information and the third one for deleting a book. The dialog windows open when the user clicks on their corresponding action button on the main window
  * The books.dat file is the json version of the information of all books available in the libraby system
  * The stylesheet.py file adds the colors and styling to the buttons and background of the application window   

# Usage

  This file 'project.py' will create the main application window. The main window has a tab for choosing among the Dashboard, Searching for a book in the informtion sysrem and information of all the books. 
  
 ## 1. Dashboard:
  
  The dashboard is the first tab of the main window. It is designed to get the information you are looking for at a glance. It allows to user to add information of a new book and editing the details of issued/unissued books. It directly gets data from the .dat file where the information of all the books is stored. (.dat file is used as storage for simplicity, the other choice is to use MongoDB for keeping the record as a leverage)
  
<p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/177114955-57cf1441-b541-4d12-b4cd-9c75593fd1eb.png">
</p>
  
  * ### Adding a new book:
   
   A new book can be created by clicking on "New Book" button. A dialog window will pop up on the screen for the user to enter a new book in the library system which requires the user to enter the information about Id, book name, its description, ISBN, Page count, if the book is issued, author name and the year the book was published:
   
<p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/177116310-0ab1d31b-fe27-4afd-ba81-a3d8c5334b2b.png">
</p>

 Adding Id is the foremost requirement but in case the user does not enter the Id, a self generated ID by the system will be allocated to the book. If the user leaves some fields empty, it will be filled as Null by the system. As the user will click on OK button, all the information will be stored in the .dat file. Along with storing, the data can be seen directly in the respective Dashboard's tables (depending upon their issuance information).
 The following image shows the entered information by the user through the add book dialog window, in the Issued books table as the user sets the Issued attribute as yes:

<p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/177119107-5c3f2e67-bc0e-42f8-89e0-4bbeca1a48ca.png">
</p>

   
 * ### Checking and updating the information of issued and unissued books:
  
  This information can be updated upon requirement. If the user wants to edit the information of any book, he/she can click on any of the attribute/cell of that book information and click on Edit button. A new Edit Book dialog window will open which allows the user to edit any attribute information of the book, except the Id as changing Id is not allowed by system. Id is the tracking key for the system so user cannot alter it.
  Suppose, the user wants to update the description of the following book:

<p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/177132324-c5c87ce1-acf0-4974-949d-6ef78e5421b8.png">
</p>
  
 The user will select the description attribute and clicks on the Edit button which will open up a new dialog window with title 'Edit Book':
  
<p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/177133191-1514ab89-6f1d-4bb5-84ad-4b959a253df0.png">
</p>

The user can enter any information he/she wants to update. In it, the user has changed the description of the book:

<p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/177133532-66cb5a7d-bbc3-48e5-89ff-ae3e9f2bc946.png">
</p>

When he clicks on the Ok button, the updated information can be seen in the respective table:

<p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/177135784-dd5c1475-1859-4f45-b0b8-0e07ce8f100a.png">
</p>

If the user wants to delete the data of any book, he/she can select the id (or any other attribute data of that record) and clicks on Delete button:

<p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/177134751-81fde92f-73f9-45c2-b366-77bd2004f40d.png">
</p>

It will open up a new dialog box for confirmation for deletion to avoid any unconcious loss of data:

<p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/177136022-5e7b7af6-f89e-4f8e-ac7a-aab7829c3924.png">
</p>

When the user clicks on OK, the data of selected book will be deleted from the system:

<p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/177136233-ef314b90-ebab-4853-9952-fba0a1cbdef5.png">
</p>

The Refresh button beside both tables will send you the most updated version of the table you're viewing. The tables will be updated automatically after each action but user can also click on Refresh button to avoid any mistake.

## 2. Find:

This tab allows the user to find the data of any book by entering its respective Id:

<p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/177136721-b314762f-fc7f-4d5a-89c9-bbf46c0c98d7.png">
</p>

The user will enter the Id, and clicks on Search button. The searched results will be shown in the table below:

<p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/177136888-c6421f6b-21a7-45ba-8abb-f896f432b189.png">
</p>

## 3. All Books:

It will show the data of all books, irrespective of the fact if they are issued or unissued. The user can view the data and clicks on Refresh button to ensure all the information about books is up-to-date:

<p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/177137426-cb6222e9-ec92-45a3-a6b1-59692fb5c72d.png">
</p>

# You might be interested:

* [PyQt5 Crash Course](https://github.com/Lizahh/PyQt5-Crash-Course-with-codes)
* [OPAC (Online Public Access Catalog) Library Management Project with Pure Python](https://github.com/Lizahh/Simplest-Library-Management-System-using-Python-Only)
* [CRUD Operations with MongoDB](https://github.com/Lizahh/CRUD-operations-with-MongoDB)
