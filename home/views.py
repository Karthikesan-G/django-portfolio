from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static


def home(request):
    about_me_details = {
        'company_details': [
            {
                "Sybrant Technologies (P) Ltd.": [
                    {
                        "job_title": "Senior Software Engineer",
                        "job_range": "Oct 2024 - Present",
                        "job_loc": "Chennai, Tamil Nadu, India"
                    }
                ],
                "Mobius Knowledge Services": [
                    {
                        "job_title": "Senior Software Engineer",
                        "job_range": "Aug 2024 - Oct 2024",
                        "job_loc": "Chennai, Tamil Nadu, India"
                    },
                    {
                        "job_title": "Software Engineer",
                        "job_range": "Jun 2023 - Jul 2024",
                        "job_loc": "Chennai, Tamil Nadu, India"
                    },
                    {
                        "job_title": "Software Engineer Trainee",
                        "job_range": "Mar 2022 - Jun 2023",
                        "job_loc": "Chennai, Tamil Nadu, India"
                    }
                ]

            }
        ],
        'educations': [
            {
                'edu_name':'E.G.S Pillay Engineering College',
                'edu_deg_grade':'Bachelor Of Engineering in Computer Science',
                'edu_loc':'Nagapattinam, Tamil Nadu, India'
            },
            {
                'edu_name':'Don Bosco Higher Secondary School',
                'edu_deg_grade':'Computer Science',
                'edu_loc':'Karaikal, Tamil Nadu, India'
            },
            {
                'edu_name':'Vidyashri High School',
                'edu_deg_grade':'',
                'edu_loc':'Karaikal, Tamil Nadu, India'
            }
        ],
        'expertises': [
            {
                'ex_name1':'Expert in',
                'ex_name2':'Data Scraping',
                'ex_con':'Extract data from websites using Python libraries like BeautifulSoup and Scrapy.',
            },
            {
                'ex_name1':'Data Analysis',
                'ex_name2':'Specialist',
                'ex_con':'Analyze datasets with Pandas and NumPy, and create visualizations with Matplotlib.',
            },
            {
                'ex_name1':'Django',
                'ex_name2':'Web Developer',
                'ex_con':'Build scalable web apps with Django for robust and efficient solutions.',
            }
        ]
    }
    return render(request,"index.html",{'about_me_details': about_me_details})
