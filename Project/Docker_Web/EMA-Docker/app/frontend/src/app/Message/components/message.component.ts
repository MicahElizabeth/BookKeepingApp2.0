import {Component} from "@angular/core";
import {OnInit} from "@angular/core";
//import { ActivatedRoute, Router } from '@angular/router';
import { Router } from '@angular/router';
import { Headers, RequestOptions} from '@angular/http';

import { UserService } from '../../user/services/user.service';

@Component({
  templateUrl: './app/Message/components/message.html',
})
export class MessageComponent implements OnInit {

  private id = "";
  private message = "";
  private pushTime = ""; //timeComplete
  private messages;
  private messageError = false;

  ngOnInit() {
    console.log("Message component initialized ...");
  }

  constructor(private userService: UserService,  private router: Router) { }

  onClickMessage() {
    let messageObject = {};

    messageObject['id'] = this.id;
    messageObject['message'] = this.message;


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

  onClickCheck() {
        this.userService.getMessages().subscribe(messages => {
          this.messages = messages.result;
        });
  }

  sendMessage(messageObject) {
    var body = messageObject;

    return this.userService.sendMessage( messageObject['id'], messageObject['message'], messageObject['pushTime']);
  }
}
