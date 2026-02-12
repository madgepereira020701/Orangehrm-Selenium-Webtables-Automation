# Orangehrm-Selenium-Webtables-Automation
Selenium automation for OrangeHRM focusing on Employee List web table operations.
Currently, the automation is implemented in **Python**. The JavaScript version will be added in a future update.
## Test Scenario being Automated
<ol>
  <li>Visit https://opensource-demo.orangehrmlive.com/</li>

  <li>Log in using the following credentials:
    <ul>
      <li>Username: Admin</li>
      <li>Password: admin123</li>
    </ul>
  </li>

  <li>Verify that login is successful by checking the Dashboard page is displayed.</li>

  <li>Click on PIM from the left-hand menu.</li>

  <li>Verify that the Employee Information page is displayed.</li>

  <li>Locate the Employee List web table.</li>

  <li>Count and print the total number of rows in the employee table.</li>

  <li>Count and print the total number of columns in the employee table.</li>

  <li>For each employee in the table, print the following details:
    <ul>
      <li>Employee ID</li>
      <li>First Name</li>
      <li>Last Name</li>
      <li>Job Title</li>
      <li>Employment Status</li>
    </ul>
  </li>

  <li>Enter <strong>Paul</strong> in the Employee Name search field.</li>

  <li>Click on the Search button.</li>

  <li>Verify that at least one employee record is displayed in the results.</li>

  <li>Verify that each result contains <strong>Paul</strong> in either the first name or last name.</li>

  <li>Select the checkbox of the first employee in the results table.</li>

  <li>Click the Delete button.</li>

  <li>Confirm the delete action in the popup.</li>

  <li>Verify that a success message is displayed.</li>

  <li>Click on Add Employee.</li>

  <li>Add a new employee using random data.</li>

  <li>Save the employee details.</li>

  <li>Navigate back to the Employee List page.</li>

  <li>Search for the newly created employee.</li>

  <li>Verify that the employee appears in the web table.</li>

  <li>Create a file named <code>employees.txt</code>.</li>

  <li>Write the first five employee records from the table to the file in the following format:
    <pre>
Employee Record:
Date: &lt;today’s date&gt;
Time: &lt;current time&gt;
Employee ID: &lt;employee id&gt;
Name: &lt;first name&gt; &lt;last name&gt;
Job Title: &lt;job title&gt;
Employment Status: &lt;status&gt;
------------------------------------------
    </pre>
  </li>

  <li>Navigate through all available pages of the employee table.</li>

  <li>Identify employees whose Job Title is QA Engineer.</li>

  <li>Print the names and employee IDs of all QA Engineers found.</li>

  <li>If no QA Engineers are found, print <strong>“No QA Engineers found.”</strong></li>

  <li>Log out of the OrangeHRM application.</li>

  <li>Close the browser.</li>
</ol>



## How to Run the Automation (Python)

Note that The automation code is available in the **`python` branch**.

<ol>
  <li>
    Switch to the <code>python</code> branch:
    <pre><code>git switch python</code></pre>
  </li>

  <li>
    Ensure the following files are present in the same directory:
    <ul>
      <li><code>main.py</code></li>
      <li><code>driver_setup.py</code></li>
      <li><code>methods.py</code></li>
    </ul>
  </li>

  <li>
    Make sure Python is installed (Python 3.9+ recommended).
  </li>

  <li>
    Install the required dependencies:
    <pre><code>pip install selenium</code></pre>
  </li>

  <li>
    Run the automation:
    <pre><code>python main.py</code></pre>
  </li>
</ol>

## Demo Video (Python)
