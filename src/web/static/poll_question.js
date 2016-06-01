function pollQuestion(classId, questionId) {
  var result = "";
  $.ajax(
  {
    url: "{% url "poll_question" %}",
    type: "GET",
    async: false,
    data: {'class_id': classId,
           'question_id': questionId},
    success: function(data) {
        result = data;
    },
  });
  return result;
}
