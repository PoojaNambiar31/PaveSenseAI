from flask import Blueprint, render_template

complaint = Blueprint(
    "complaint",
    __name__
)

@complaint.route("/upload")
def upload():
    return render_template("complaint/upload.html")


@complaint.route("/applicant")
def applicant():
    return render_template("complaint/applicant.html")


@complaint.route("/address")
def address():
    return render_template("complaint/address.html")


@complaint.route("/road-details")
def road_details():
    return render_template("complaint/road_details.html")


@complaint.route("/incident")
def incident():
    return render_template("complaint/incident.html")


@complaint.route("/analysis")
def analysis():
    return render_template("complaint/analysis.html")


@complaint.route("/preview")
def preview():
    return render_template("complaint/preview.html")


@complaint.route("/submit")
def submit():
    return render_template("complaint/submit.html")


@complaint.route("/success")
def success():
    return render_template("complaint/success.html")