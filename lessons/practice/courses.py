from __future__ import annotations

class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, pre: str) -> bool:
         if self.level >= 400 and pre in self.prerequisites:
              return True
         else:
              return False
        
def find_courses(inp_list: list[Course], pre: str) -> list[str]:
        return_list: list[str] = []
        for course in range(len(inp_list)):
            if inp_list[course].is_valid_course(pre):
                return_list.append(inp_list[course].name)
        return return_list