#include "main.h"

bool zeromq_boolRunning = false;

char zeromq_charMode[256] = { };
char zeromq_charName[256] = { };

void zeromq_start(char* charMode, char* charName) {
	{
		assert(strlen(charName) < 16);
		
		assert(strstr(charName, " ") == NULL);
	}
	
	{
		zeromq_boolRunning = true;
	}
	
	{
		strcpy(zeromq_charMode, charMode);
		
		strcpy(zeromq_charName, charName);
	}
	
	{
		void* contextHandle = zmq_ctx_new();
		void* socketHandle = zmq_socket(contextHandle, ZMQ_PAIR);
		
		{
			if (strcmp(zeromq_charMode, "tcp") == 0) {
				if (zmq_bind(socketHandle, "tcp://*:54361") == -1) {
					printf("zeromq: %s\n", zmq_strerror(zmq_errno()));
				}
				
			} else if (strcmp(zeromq_charMode, "ipc") == 0) {
				if (zmq_bind(socketHandle, "ipc:///tmp/minichess-zeromq") == -1) {
					printf("zeromq: %s\n", zmq_strerror(zmq_errno()));
				}
				
			}
		}
		
		{
			do {
				cJSON* cjsonIn = NULL;
				cJSON* cjsonOut = cJSON_CreateObject();
				
				{
					char charJson[1024] = { };
					
					if (zmq_recv(socketHandle, charJson, sizeof(charJson), 0) == -1) {
						printf("zeromq: %s\n", zmq_strerror(zmq_errno()));
					}
					
					cjsonIn = cJSON_Parse(charJson);
				}
				
				{
					if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "ping") == 0) {
						cJSON_AddStringToObject(cjsonOut, "strOut", zeromq_charName);
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_reset") == 0) {
						chess_reset();
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_boardGet") == 0) {
						char charOut[1024] = { };
						
						chess_boardGet(charOut);
						
						cJSON_AddStringToObject(cjsonOut, "strOut", charOut);
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_boardSet") == 0) {
						char charIn[1024] = { };
						
						strcpy(charIn, cJSON_GetObjectItem(cjsonIn, "strIn")->valuestring);
						
						chess_boardSet(charIn);
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_winner") == 0) {
						char charReturn[16] = { };
						
						charReturn[0] = chess_winner();
						charReturn[1] = '\0';
						
						cJSON_AddStringToObject(cjsonOut, "strReturn", charReturn);
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_isValid") == 0) {
						cJSON_AddBoolToObject(cjsonOut, "boolReturn", chess_isValid(cJSON_GetObjectItem(cjsonIn, "intX")->valueint, cJSON_GetObjectItem(cjsonIn, "intY")->valueint));
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_isEnemy") == 0) {
						char charIn[16] = { };
						
						strcpy(charIn, cJSON_GetObjectItem(cjsonIn, "strPiece")->valuestring);
						
						cJSON_AddBoolToObject(cjsonOut, "boolReturn", chess_isEnemy(charIn[0]));
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_isOwn") == 0) {
						char charIn[16] = { };
						
						strcpy(charIn, cJSON_GetObjectItem(cjsonIn, "strPiece")->valuestring);
						
						cJSON_AddBoolToObject(cjsonOut, "boolReturn", chess_isOwn(charIn[0]));
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_isNothing") == 0) {
						char charIn[16] = { };
						
						strcpy(charIn, cJSON_GetObjectItem(cjsonIn, "strPiece")->valuestring);
						
						cJSON_AddBoolToObject(cjsonOut, "boolReturn", chess_isNothing(charIn[0]));
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_eval") == 0) {
						cJSON_AddNumberToObject(cjsonOut, "intReturn", chess_eval());
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_moves") == 0) {
						int intOut = 0;
						char charOut[1024] = { };
						
						intOut = chess_moves(charOut);
						
						cJSON_AddNumberToObject(cjsonOut, "intOut", intOut);
						cJSON_AddStringToObject(cjsonOut, "strOut", charOut);
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_movesShuffled") == 0) {
						int intOut = 0;
						char charOut[1024] = { };
						
						intOut = chess_movesShuffled(charOut);
						
						cJSON_AddNumberToObject(cjsonOut, "intOut", intOut);
						cJSON_AddStringToObject(cjsonOut, "strOut", charOut);
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_movesEvaluated") == 0) {
						int intOut = 0;
						char charOut[1024] = { };
						
						intOut = chess_movesEvaluated(charOut);
						
						cJSON_AddNumberToObject(cjsonOut, "intOut", intOut);
						cJSON_AddStringToObject(cjsonOut, "strOut", charOut);
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_move") == 0) {
						char charIn[16] = { };
						
						strcpy(charIn, cJSON_GetObjectItem(cjsonIn, "strIn")->valuestring);
						
						chess_move(charIn);
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_moveRandom") == 0) {
						char charOut[16] = { };
						
						chess_moveRandom(charOut);
						
						cJSON_AddStringToObject(cjsonOut, "strOut", charOut);
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_moveGreedy") == 0) {
						char charOut[16] = { };
						
						chess_moveGreedy(charOut);
						
						cJSON_AddStringToObject(cjsonOut, "strOut", charOut);
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_moveNegamax") == 0) {
						char charOut[16] = { };
						
						chess_moveNegamax(charOut, cJSON_GetObjectItem(cjsonIn, "intDepth")->valueint, cJSON_GetObjectItem(cjsonIn, "intDuration")->valueint);
						
						cJSON_AddStringToObject(cjsonOut, "strOut", charOut);
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_moveAlphabeta") == 0) {
						char charOut[16] = { };
						
						chess_moveAlphabeta(charOut, cJSON_GetObjectItem(cjsonIn, "intDepth")->valueint, cJSON_GetObjectItem(cjsonIn, "intDuration")->valueint);
						
						cJSON_AddStringToObject(cjsonOut, "strOut", charOut);
						
					} else if (strcmp(cJSON_GetObjectItem(cjsonIn, "strFunction")->valuestring, "chess_undo") == 0) {
						chess_undo();
						
					}
				}
				
				{
					char* charJson = cJSON_PrintUnformatted(cjsonOut);
					
					if (zmq_send(socketHandle, charJson, strlen(charJson), 0) == -1) {
						printf("zeromq: %s\n", zmq_strerror(zmq_errno()));
					}
					
					free(charJson);
				}
				
				cJSON_Delete(cjsonIn);
				cJSON_Delete(cjsonOut);
			} while (zeromq_boolRunning == true);
		}
		
		zmq_close(socketHandle);
		zmq_ctx_destroy(contextHandle);
	}
}

void zeromq_stop() {
	{
		zeromq_boolRunning = false;
	}
}
