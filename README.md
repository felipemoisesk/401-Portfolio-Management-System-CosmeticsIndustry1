<h1 align="center">
     <a> 401-Portfolio-Management-System-CosmeticsIndustry1 </a>
</h1>

<h4 align="center">
🚧 OCT/21 to MAR/22 🚀 🚧
</h4>

## 💻 About the project

The Portfolio Management System, or SGP, is a system developed for the Portfolio & Categories core, Market Intelligence Directorate, which offers a detailed view of the retail portfolio, at the SKU level, considering the collection, processing, democratization and data analysis for the company's stakeholders.

The following tool covers the ETL phase of the project, collecting and processing data from various company systems, made available after extraction in .xlsx or .csv files, mostly.

The construction of this tool reduced processing time by 87% compared to the original solution that was developed in Excel by the team previously responsible, from +8h to less than 1h, considering the beginning of processing until the final delivery with pre-analysis and tool print shop.

In order to meet the needs of a team mainly composed of people with business skills, Microsoft SharePoint was chosen as a repository of raw, processed and refined files, emulating a layered environment (Bronze, Silver and Gold) already known in ETL pipelines. in data engineering.

As part of the data analysis, dashboards in Tableau and PowerBI were made available to the team, including dimensional data modeling in both.

The project brings value and autonomy to the business team, from ETL to self-consumption of data and team analytics.

## ⚙️ Features

- [x] **ETL Automation**:
  - [x] creation of datamart, localhost and Microsoft SharePoint, in Bronze, Silver and Gold layers:
    - bronze: data extracted from the systems in TXT, XLSX and CSV formats
    - silver: data treated, cleaned and organized in tabular files
    - gold: refined data, with dimensional modeling applied for input into the company's dataviz tools
  - [x] interaction between script and user:
    - navigation between modules and sub-modules that you want to update in an interactive and instructed way, through questions and selection of answers

- [x] **Tool built on interconnected modules**:
  - [x] Financial Performance module
    - geographic regions
    - commercial regions
    - sales channels
  - [x] Commercial Planning module
    - geographic regions
    - sales channels

---

## 🚀 How to run the tool


When executing the scripts, the user will receive questions on the execution screen about the modules he wants to update.

However, this tool is composed of three stages:

1. Collection of company transactional information, via xlsx/txt/csv, or reports generated in the various company systems and departments (Bronze layer insertion)
2. Automated python script execution for processing, data cleaning, data dimensional modeling and data file pre-organization (Silver layer insertion)
3. Availability in repository, output, of the data treated according to business requirements (insertion Gold layer)

💡 Data visualization via Tableau or PowerBi uses the output of the tool's Gold layer.

### Prerequisites

As it is a tool that works locally, before starting, you will need to download this project on your machine, so that the repositories will already be linked to the project directory. Also, I recommend downloading [Git](https://git-scm.com) for version control. About the IDE, I used [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=linux).

---

## 🛠 Technologies

The following tools were used in building the project:

#### **ETL** ([Python](https://www.python.org/))

- **[Pandas](https://pandas.pydata.org/)**
- **[NumPy](https://github.com/ReactTraining/react-router/tree/master/packages/react-router-dom)**
- **[OS](https://docs.python.org/3/library/os.html)**
- **[Matplotlib](https://matplotlib.org/)**

### **Data Visualization**

- **[Tableau](https://www.tableau.com/)**
- **[PowerBI](https://powerbi.microsoft.com/pt-br/)**

### **Data Repository**

- **[Microsoft SharePoint](https://www.microsoft.com/pt-br/microsoft-365/sharepoint/collaboration)**

#### **Utilities**

- Editor: **[PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=linux)**

---

## 📝 License

This project is licensed under [MIT](./LICENSE).

Made with ❤️ by Felipe Möises 👋🏽 [Get in touch!](https://www.linkedin.com/in/felipemoises/)

---

## README Versions

[French 🇫🇷](./README-FR.md) | [Portuguese 🇧🇷](./README-PT.md)
