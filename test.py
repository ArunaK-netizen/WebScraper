import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Base URL for Naukri search (for demonstration; use a real URL based on your search criteria)
url = "https://www.naukri.com/software-developer-jobs" 

# Send request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize lists to store extracted data
company_names = []
job_titles = []
job_descriptions = []
key_responsibilities = []
required_skills = []
qualifications = []
tools_technologies = []
experience_levels = []
locations = []
salary_ranges = []
sources = []

# Sample extraction (structure might vary by page; adjust accordingly)
for job_card in soup.find_all('article', class_='jobTuple bgWhite br4 mb-8'):
    try:
        company_name = job_card.find('a', class_='subTitle ellipsis fleft').get_text(strip=True)
        company_names.append(company_name)

        job_title = job_card.find('a', class_='title fw500 ellipsis').get_text(strip=True)
        job_titles.append(job_title)

        job_description = job_card.find('div', class_='job-description fs12 grey-text').get_text(strip=True)
        job_descriptions.append(job_description)

        key_responsibility = " ".join([li.get_text(strip=True) for li in job_card.find_all('li', class_='responsibility')])
        key_responsibilities.append(key_responsibility)

        required_skill = job_card.find('span', class_='ellipsis fleft fs12 lh16').get_text(strip=True)
        required_skills.append(required_skill)

        experience_level = job_card.find('li', class_='experience').get_text(strip=True)
        experience_levels.append(experience_level)

        location = job_card.find('li', class_='location').get_text(strip=True)
        locations.append(location)

        salary = job_card.find('li', class_='salary').get_text(strip=True) if job_card.find('li', class_='salary') else "Not disclosed"
        salary_ranges.append(salary)

        sources.append("Naukri.com")

        # Random sleep to mimic human behavior
        time.sleep(random.uniform(1, 3))

    except AttributeError:
        # Handle missing data gracefully
        continue

# Save data to a DataFrame
data = pd.DataFrame({
    "Company Name": company_names,
    "Job Title": job_titles,
    "Job Description": job_descriptions,
    "Key Responsibilities": key_responsibilities,
    "Required Skills": required_skills,
    "Experience Level": experience_levels,
    "Location": locations,
    "Salary Range": salary_ranges,
    "Source": sources
})

# Save to CSV
data.to_csv("naukri_jobs.csv", index=False)
print("Scraping completed and data saved to naukri_jobs.csv")
