from flask import Flask, jsonify,request

app = Flask(__name__)

# Route to return student number in JSON format
@app.route('/')
def get_student_number():
    student_number = 200567867  # Replace with your actual student number
    return jsonify({"My student number is": student_number})

# Route for Dialogflow webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
   # fulfillmentText = 'xxx'
    #query_result = req.get('queryResult')
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName')

    if intent == 'Vision System Calibration':  # Replace 'YourIntentName' with the actual intent name
        machine_model = req.get('queryResult').get('parameters').get('MachineModelNumber')
        lens_manufacturer = req.get('queryResult').get('parameters').get('LensManufacturer')
        camera_manufacturer = req.get('queryResult').get('parameters').get('CameraManufacturer')

        response = {
            "fulfillmentText": f"Absolutely! The vision system calibration procedure for the machine, having model number {machine_model}, is detailed below. It features a {camera_manufacturer} camera and a {lens_manufacturer} lens./n1) Ensure the machine is in a stable and controlled environment with consistent lighting conditions./n2) Clear any obstructions or debris that may interfere with the vision system./n3) Place the label in front of the camera's field of view./n4)Please make sure that distance between camera and object should be from 7 to 19mm./n5) After calibration, validate the results with actual image./nWould you like to explore additional assistance or information about the machine?"
        }
    else:
        response = {"fulfillmentText": "Sorry, I did not understand that."}

    return jsonify(response)

'''def get_entity_value(request_json, entity_name):
    entities = request_json.get('queryResult', {}).get('parameters', {}).get(entity_name, [])
    if entities:
        return entities[0].get('resolvedValue', None)
    else:
        return None
    intent_name = req.get('queryResult').get('intent').get('displayName')
    if intent_name == 'Emergency Shutdown Procedure':
       
         response = {
                    "fulfillmentText": "Certainly! Here are the emergency shutdown procedure steps for a labelling machine \n1) Press the Emergency Stop button on the control panel.\n2) Turn off the main power switch.\n3) Unplug the power cord or shut down the main power supply.\n4) Ensure to isolate utilities such as air to prevent any potential hazards or further damage.\n5) Remove the products from the machine.\n6) Adhere to emergency protocols and procedures.\n7) Record incident details for analysis.\n8) Perform safety checks before restarting.\n9) If unsure, seek professional assistance.\nDo you need further assistance with the machine?"
                    }

    else:
       
        response = {"fulfillmentText": "Sorry, I did not understand that."}

    return jsonify(response)
    if query_result.get('action') == 'get.address':
        ### Perform set of executable code
        ### if required
        ### ...

        fulfillmentText = "Hi .. i am in"
    return {
            "fulfillmentText": fulfillmentText,
            "source": "webhookdata"
        }'''

if __name__ == '__main__':
    app.run(debug=True)
