import {Component} from "@angular/core";
import {OnInit} from "@angular/core";
//import { ActivatedRoute, Router } from '@angular/router';
import { Router } from '@angular/router';
import { Headers, RequestOptions} from '@angular/http';

import { UserService } from '../../user/services/user.service';

@Component({
  templateUrl: './app/Survey/components/survey.html',
})
export class SurveyComponent implements OnInit {

  private id = "";
  private message = ""; //response
  private question = "";
  private qtype = "";
  private pushTime = ""; //timeComplete
  private questions;
  private messages;
  private messageError = false;

  ngOnInit() {
    console.log("Survey component initialized ...");
  }

  constructor(private userService: UserService,  private router: Router) { }

  onClickAddMessage() {
    let messageObject = {};

    messageObject['id'] = this.id;
    messageObject['message'] = this.message;
    messageObject['pushTime'] = this.pushTime;


    this.sendMessage(messageObject)
      .subscribe(
      data => {
        this.messageError = false;
      },
      err => {
        this.messageError = true;
        console.log('error');
      },
      () => console.log('finished'));
  }

  onClickAddQuestion() {
    let questionObject = {};

    questionObject['id'] = this.id;
    questionObject['question'] = this.question;
    questionObject['qtype'] = this.qtype;
    questionObject['pushTime'] = this.pushTime;

    this.sendQuestion(questionObject)
      .subscribe(
      data => {
        this.messageError = false;
      },
      err => {
        this.messageError = true;
        console.log('error');
      },
      () => console.log('finished'));
  }

  onClickCheckMessages() {
        this.userService.getMessages().subscribe(messages => {
          this.messages = messages.result;
        });
  }

  onClickCheckQuestions() {
    this.userService.getQuestions().subscribe(questions => {
      this.questions = questions.result;
    });
  }

  sendMessage(messageObject) {
    var body = messageObject;

    return this.userService.sendMessage(  messageObject['id'], messageObject['message'], messageObject['pushTime']);
  }

  sendQuestion(questionObject) {
    var body = questionObject;
    //  tslint:disable:max-line-length

    return this.userService.sendQuestion(  questionObject['id'], questionObject['question'], questionObject['qtype'],
    questionObject['pushTime']);

    // tslint:enable:max-line-length

  }
}
