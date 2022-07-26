import pandas as pd
def get_skills():
    career_builder=pd.read_json('skills')
    skills=career_builder['skills']
    skills=pd.DataFrame(skills)
    list_skills=skills.values.ravel().tolist()
    return list_skills
list_skills=get_skills()

#Real time function to collect data
def get_job():
    career_builder=pd.read_json('jobs')
    job=career_builder['description']
    job=job.tolist()
    #x=job[-1]
    return job
#x=get_job()
job=get_job()