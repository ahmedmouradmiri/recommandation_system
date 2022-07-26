import pandas as pd
def get_skills():
    career_builder=pd.read_json('career_builder_jobs_10501-Copy1.json')
    skills=career_builder['skills']
    skills=pd.DataFrame(skills)
    list_skills=skills.values.ravel().tolist()
    return list_skills
list_skills=get_skills()

#Real time function to collect data
def get_job():
    career_builder=pd.read_json('career_builder_jobs_10501-Copy1.json')
    job=career_builder['description']
    job=job.tolist()
    x=job[-1]
    return x
x=get_job()