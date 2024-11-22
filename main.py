# from fastapi import FastAPI, UploadFile, HTTPException
# import pandas as pd
# from utils.analyze import analyze_sales_data_local, summarize_team_performance
# import io
# import logging

# # FastAPI application object
# app = FastAPI()

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Placeholder for in-memory data
# data_store = None


# @app.post("/upload-data/")
# async def upload_data(file: UploadFile):
#     """
#     Endpoint to upload sales data.
#     """
#     global data_store
#     try:
#         contents = await file.read()
#         if file.filename.endswith(".csv"):
#             data_store = pd.read_csv(io.BytesIO(contents), sep="\t")  # Assuming tab-separated CSV
#             logger.info(f"Data uploaded successfully: {file.filename}")
#             logger.info(f"Uploaded Data Shape: {data_store.shape}")
#             logger.info(f"Uploaded Data Columns: {list(data_store.columns)}")
#         else:
#             raise HTTPException(status_code=400, detail="Only CSV files are supported.")
#         return {"message": "Data uploaded successfully."}
#     except Exception as e:
#         logger.error(f"Error during file upload: {e}")
#         raise HTTPException(status_code=500, detail=f"Failed to upload data: {str(e)}")


# @app.get("/api/rep_performance/")
# async def rep_performance(employee_id: int):
#     """
#     Endpoint to analyze a specific sales representative's performance.
#     """
#     if data_store is None:
#         logger.warning("No data uploaded")
#         raise HTTPException(status_code=400, detail="No data uploaded.")
    
#     rep_data = data_store[data_store['employee_id'] == employee_id]
#     if rep_data.empty:
#         logger.warning(f"Sales representative with ID {employee_id} not found.")
#         raise HTTPException(status_code=404, detail="Sales representative not found.")
    
#     logger.info(f"Filtering data for employee_id: {employee_id}")
#     logger.info(f"Filtered Data: {rep_data}")
#     summary = rep_data.describe(include='all').to_string()
#     try:
#         feedback = analyze_sales_data_local(rep_data)
#         logger.info(f"Feedback generated for rep {employee_id}")
#     except Exception as e:
#         logger.error(f"Error generating feedback for rep {employee_id}: {e}")
#         raise HTTPException(status_code=500, detail="Failed to analyze sales data.")

#     return {"rep_id": employee_id, "feedback": feedback}


# @app.get("/api/team_performance/")
# async def team_performance():
#     """
#     Endpoint to analyze team performance.
#     """
#     if data_store is None:
#         logger.warning("No data uploaded")
#         raise HTTPException(status_code=400, detail="No data uploaded.")
    
#     try:
#         feedback = summarize_team_performance(data_store)
#         logger.info("Feedback generated for team performance.")
#     except Exception as e:
#         logger.error(f"Error generating feedback for team performance: {e}")
#         raise HTTPException(status_code=500, detail="Failed to analyze team performance.")

#     return {"team_feedback": feedback}


from fastapi import FastAPI, UploadFile, HTTPException
import pandas as pd
from utils.analyze import analyze_rep_performance, summarize_team_performance, analyze_trends
from utils.llm import generate_feedback
import io
import logging

# FastAPI application object
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Placeholder for in-memory data
data_store = None

@app.post("/upload-data/")
async def upload_data(file: UploadFile):
    """
    Endpoint to upload sales data (CSV/JSON format).
    """
    global data_store
    try:
        contents = await file.read()
        # Detect delimiter and parse CSV
        if file.filename.endswith(".csv"):
            data_store = pd.read_csv(io.BytesIO(contents), sep=None, engine='python')
        elif file.filename.endswith(".json"):
            data_store = pd.read_json(io.BytesIO(contents))
        else:
            raise HTTPException(status_code=400, detail="Only CSV or JSON files are supported.")
        
        # Log details for debugging
        logger.info(f"Data uploaded successfully: {file.filename}")
        logger.info(f"Uploaded Data Shape: {data_store.shape}")
        logger.info(f"Uploaded Data Columns: {list(data_store.columns)}")
        return {"message": "Data uploaded successfully."}
    except Exception as e:
        logger.error(f"Error during file upload: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to upload data: {str(e)}")


# @app.post("/upload-data/")
# async def upload_data(file: UploadFile):
#     """
#     Endpoint to upload sales data (CSV/JSON format).
#     """
#     global data_store
#     try:
#         contents = await file.read()
#         if file.filename.endswith(".csv"):
#             data_store = pd.read_csv(io.BytesIO(contents))
#         elif file.filename.endswith(".json"):
#             data_store = pd.read_json(io.BytesIO(contents))
#         else:
#             raise HTTPException(status_code=400, detail="Only CSV or JSON files are supported.")
#         logger.info(f"Data uploaded successfully: {file.filename}")
#         logger.info(f"Uploaded Data Shape: {data_store.shape}")
#         logger.info(f"Uploaded Data Columns: {list(data_store.columns)}")
#         return {"message": "Data uploaded successfully."}
#     except Exception as e:
#         logger.error(f"Error during file upload: {e}")
#         raise HTTPException(status_code=500, detail=f"Failed to upload data: {str(e)}")


@app.get("/api/rep_performance/")
async def rep_performance(employee_id: int):
    """
    Endpoint to analyze a specific sales representative's performance.
    """
    if data_store is None:
        logger.warning("No data uploaded")
        raise HTTPException(status_code=400, detail="No data uploaded.")
    
    rep_data = data_store[data_store['employee_id'] == employee_id]
    if rep_data.empty:
        logger.warning(f"Sales representative with ID {employee_id} not found.")
        raise HTTPException(status_code=404, detail="Sales representative not found.")
    
    feedback = analyze_rep_performance(rep_data)
    return {"rep_id": employee_id, "feedback": feedback}


@app.get("/api/team_performance/")
async def team_performance():
    """
    Endpoint to analyze team performance.
    """
    if data_store is None:
        logger.warning("No data uploaded")
        raise HTTPException(status_code=400, detail="No data uploaded.")
    
    feedback = summarize_team_performance(data_store)
    return {"team_feedback": feedback}


@app.get("/api/performance_trends/")
async def performance_trends(time_period: str = "monthly"):
    """
    Endpoint to analyze trends and forecast performance.
    """
    if data_store is None:
        logger.warning("No data uploaded")
        raise HTTPException(status_code=400, detail="No data uploaded.")
    
    feedback = analyze_trends(data_store, time_period)
    return {"trends_feedback": feedback}
