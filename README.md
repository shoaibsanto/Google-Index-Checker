<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Google Indexing Status Checker</h1>
<p>This repository contains a Python script that checks if a list of domains is indexed by Google using the "site:" operator and stores the results in a CSV file.</p>

<h2>Features</h2>
<ul>
    <li>Reads domains from a <code>urls.txt</code> file.</li>
    <li>Uses Google Search to check if each domain is indexed.</li>
    <li>Saves the index status for each domain in a <code>index_status.csv</code> file.</li>
</ul>

<h2>Prerequisites</h2>
<p>Before running the script, ensure you have the following installed:</p>
<ol>
    <li><strong>Python 3.x</strong></li>
    <li><strong>Required Packages:</strong></li>
    <ul>
        <li><code>googlesearch-python</code></li>
        <li><code>csv</code></li>
    </ul>
</ol>
<p>You can install the required packages by running:</p>
<pre><code>pip install googlesearch-python</code></pre>

<h2>Usage</h2>

<h3>1. Prepare a list of URLs</h3>
<p>Create a <code>urls.txt</code> file in the root directory of your project. Add the domains you want to check in this file, each on a new line.</p>
<p>Example of <code>urls.txt</code>:</p>
<pre><code>example.com
anotherexample.com
website.org
</code></pre>

<h3>2. Run the Script</h3>
<p>Execute the Python script by running the following command:</p>
<pre><code>python check_index_status.py</code></pre>

<h3>3. Output</h3>
<p>After running the script, the results will be saved in a file named <code>index_status.csv</code>. This file will contain two columns:</p>
<ul>
    <li><code>urls</code>: The domain that was checked.</li>
    <li><code>index_status</code>: Either <code>Indexed</code> or <code>Not Indexed</code>, based on whether the domain is found in Google search.</li>
</ul>

<h3>Sample Output</h3>
<p>If the <code>urls.txt</code> contains:</p>
<pre><code>example.com
anotherexample.com
</code></pre>
<p>The <code>index_status.csv</code> will look like this:</p>
<pre><code>urls,index_status
example.com,Indexed
anotherexample.com,Not Indexed
</code></pre>

<h2>Error Handling</h2>
<p>In case the script encounters any errors during the search process (e.g., issues with network connectivity), it will print the error message in the console.</p>

<h2>Customization</h2>
<p>You can modify the <code>tld</code>, <code>num</code>, <code>stop</code>, and <code>pause</code> parameters in the search query to customize the behavior of Google search results.</p>
<p>The script currently checks one result per domain (<code>num=1</code>). If you want more results, you can modify the <code>num</code> parameter.</p>

<hr>
<p>Feel free to modify or extend the script to fit your specific use case!</p>

</body>
</html>
